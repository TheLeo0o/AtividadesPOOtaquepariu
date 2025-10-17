from bebidas import Espresso, CafeCoado, CafePretinhoTradicional

def test_espresso_preco():
    bebida = Espresso()
    assert bebida.preco() == 4.00
    assert bebida.get_descricao() == "Espresso"

def test_cafe_coado_preco():
    bebida = CafeCoado()
    assert bebida.preco() == 3.50

def test_cafe_pretinho_erro():
    bebida = CafePretinhoTradicional()
    try:
        bebida.decorado = True
    except Exception as e:
        assert "Não é permitido" in str(e)
