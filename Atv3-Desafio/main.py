from bebidas import Espresso, CafeCoado, CafePretinhoTradicional
from cafeteria import Leite, Caramelo, Canela, TamanhoGrande, LeiteVegetal, Chocolate, Adoçante, Chantilly

pedido_d = TamanhoGrande(Canela(Caramelo(Leite(Espresso()))))
print("Pedido D:", pedido_d.get_descricao())
print("Preço: R$", f"{pedido_d.preco():.2f}\n")

pedido_e = Adoçante(Chocolate(LeiteVegetal(CafeCoado())))
print("Pedido E:", pedido_e.get_descricao())
print("Preço: R$", f"{pedido_e.preco():.2f}\n")

try:
    pedido_f = Chantilly(CafePretinhoTradicional())
except Exception as e:
    print("Pedido F: Erro ->", e)
