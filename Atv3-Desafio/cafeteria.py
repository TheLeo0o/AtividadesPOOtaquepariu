from bebidas import Bebida

class Adicional(Bebida):
    def __init__(self, bebida: Bebida):
        if hasattr(bebida, "personalizavel") and bebida.personalizavel is False:
            raise Exception("Não é permitido adicionar complementos ao Café Pretinho Tradicional!")
        super().__init__()
        self.bebida = bebida

class Leite(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} com Leite"

    def preco(self) -> float:
        return self.bebida.preco() + 1.00

class LeiteVegetal(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} com Leite Vegetal"

    def preco(self) -> float:
        return self.bebida.preco() + 1.50

class EspumaLeite(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} com Espuma de Leite"

    def preco(self) -> float:
        return self.bebida.preco() + 0.75

class Chocolate(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} com Chocolate"

    def preco(self) -> float:
        return self.bebida.preco() + 1.25

class Caramelo(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} com Caramelo"

    def preco(self) -> float:
        return self.bebida.preco() + 1.00

class Canela(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} com Canela"

    def preco(self) -> float:
        return self.bebida.preco() + 0.50

class Chantilly(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} com Chantilly"

    def preco(self) -> float:
        return self.bebida.preco() + 1.00


class Adoçante(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} com Adoçante"

    def preco(self) -> float:
        return self.bebida.preco()  


class DoseExtraCafe(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} com Dose Extra de Café"

    def preco(self) -> float:
        return self.bebida.preco() + 2.00
    
class TamanhoGrande(Adicional):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()} Tamanho Grande"

    def preco(self) -> float:
        return round(self.bebida.preco() * 1.3, 2)
