from bebidas import Espresso, CafeCoado, CafePretinhoTradicional
from cafeteria import Leite, Caramelo, Canela, TamanhoGrande, LeiteVegetal, Chocolate, Adoçante, Chantilly

def test_pedido_d():
    bebida = TamanhoGrande(Canela(Caramelo(Leite(Espresso()))))
    assert "Canela" in bebida.get_descricao()
    assert round(bebida.preco(), 2) == 8.45

def test_pedido_e():
    bebida = Adoçante(Chocolate(LeiteVegetal(CafeCoado())))
    assert "Adoçante" in bebida.get_descricao()
    assert round(bebida.preco(), 2) == 6.25

def test_pedido_f_erro():
    try:
        Chantilly(CafePretinhoTradicional())
        assert False, "Deveria lançar exceção"
    except Exception as e:
        assert "Não é permitido" in str(e)
