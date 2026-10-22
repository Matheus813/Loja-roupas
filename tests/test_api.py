import pytest
from fastapi.testclient import TestClient

from api import app

cliente = TestClient(app)   # faz pedidos HTTP sem abrir porta


@pytest.fixture(autouse=True)
def carrinho_vazio():
    cliente.delete("/carrinho")   # cada teste começa do zero


def test_vitrine_tem_tres_produtos():
    resposta = cliente.get("/produtos")
    assert resposta.status_code == 200
    assert len(resposta.json()) == 3


def test_produto_inexistente_da_404():
    resposta = cliente.get("/produtos/99")
    assert resposta.status_code == 404


def test_filtro_por_tamanho():
    resposta = cliente.get("/produtos", params={"tamanho": "M"})
    nomes = [p["nome"] for p in resposta.json()]
    assert nomes == ["Camiseta básica"]


def test_quantidade_zero_da_422():
    resposta = cliente.post("/carrinho/itens", json={"produto_id": 1, "quantidade": 0})
    assert resposta.status_code == 422


def test_adicionar_item_da_201():
    resposta = cliente.post("/carrinho/itens", json={"produto_id": 1, "quantidade": 3})
    assert resposta.status_code == 201
    assert resposta.json()["pecas_no_carrinho"] == 3


def test_total_com_promocao_sem_frete():
    cliente.post("/carrinho/itens", json={"produto_id": 1, "quantidade": 3})
    cliente.post("/carrinho/itens", json={"produto_id": 2, "quantidade": 1})
    assert cliente.get("/carrinho/total").json() == {
        "pecas": 4, "subtotal": 249.6, "total": 224.64}


def test_total_abaixo_de_200_paga_frete():
    cliente.post("/carrinho/itens", json={"produto_id": 1, "quantidade": 1})
    assert cliente.get("/carrinho/total").json()["total"] == 50.91

@pytest.fixture(autouse=True)
def banco_de_teste():
    """Cada teste ganha um banco novo, na memória, com os 3 produtos."""
    engine = engine_em_memoria()
    criar_tabelas(engine)
    with Session(engine) as sessao:
        popular_se_vazio(ServicoCatalogo(RepositorioProdutos(sessao)))

def sessao_de_teste():
    with Session(engine) as sessao:
        yield sessao

    app.dependency_overrides[obter_sessao] = sessao_de_teste
    cliente.delete("/carrinho")
    yield
    app.dependency_overrides.clear()