from abc import ABC, abstractmethod

class Bebida(ABC):
    def __init__(self):
        self.descricao: str = "Bebida desconhecida"

    def get_descricao(self) -> str:
        return self.descricao

    @abstractmethod
    def preco(self) -> float:
        pass

class Espresso(Bebida):
    def __init__(self):
        super().__init__()
        self.descricao = "Espresso"

    def preco(self) -> float:
        return 4.00
    
class CafeCoado(Bebida):
    def __init__(self):
        super().__init__()
        self.descricao = "Café Coado"

    def preco(self) -> float:
        return 3.50
    
class Descafeinado(Bebida):
    def __init__(self):
        super().__init__()
        self.descricao = "Descafeinado"

    def preco(self) -> float:
        return 4.50
    
class CafePretinhoTradicional(Bebida):
    def __init__(self):
        super().__init__()
        self.descricao = "Café Pretinho Tradicional"
        self.personalizavel = False

    def preco(self) -> float:
        return 2.00

    def __setattr__(self, name, value):
        if hasattr(self, "descricao") and name == "decorado":
            raise Exception("Não é permitido adicionar complementos ao Café Pretinho Tradicional!")
        super().__setattr__(name, value)
