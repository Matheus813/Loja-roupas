from sqlmodel import Session
from loja.banco import criar_engine, criar_tabelas
from loja.produto import Produto
from loja.repositorio import RepositorioProdutos

def test_dados_sobrevivem_ao_reinicio(tmp_path):
    url = f"qlite:///{tmp_path / 'loja.db'}"
    engine = criar_engine(url)
    criar_tabelas(engine)
    with Session(engine) as sessao:
        RepositorioProdutos(sessao).adicionar(Produto("Moleton", 159.90, "P"))
    engine.dispose()

    outro = criar_engine(url)
    with Session(outro) as sessao:
        assert RepositorioProdutos(sessao).buscar(1).nome == "Moleton"