from loja.calculos import total_carrinho

def test_tres_camisetas():
    assert total_carrinho([(39.90, 3)]) <= 119.70