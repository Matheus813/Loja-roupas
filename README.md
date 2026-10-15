# Loja de Roupas

Projeto construído passo a passo na aula de Coding (Faculdade Senac Pernambuco, 2026.2).

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v
fastapi dev api.py              # abre a API em http://127.0.0.1:8000/docs
```

![testes](https://github.com/SEU-USUARIO/loja-roupas/actions/workflows/testes.yml/badge.svg)

## O que tem aqui

| Pasta ou arquivo | O que é | Aula |
|---|---|---|
| `vitrine.py` | os dados da loja em listas e dicionários | 3 |
| `loja/calculos.py` | total do carrinho e frete, com testes | 4 |
| `loja/produto.py` | Produto, Camiseta e Calça | 6 e 7 |
| `loja/carrinho.py` | o Carrinho, que tem produtos e uma promoção | 6 e 7 |
| `loja/promocao.py` | o contrato Promocao e três promoções | 7 e 8 |
| `.github/workflows/testes.yml` | o GitHub roda os testes a cada push | 8 |
| `api.py` | a loja como API: vitrine, filtro, carrinho e total | 9 |
| `tests/test_api.py` | testes da API com TestClient | 9 |