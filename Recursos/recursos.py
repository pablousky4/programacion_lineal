from .Comida import Comida
from .Madera import Madera
from .Oro import Oro

class Recursos:
    def __init__(self, comida, madera, oro):
        self.comida = Comida(comida)
        self.madera = Madera(madera)
        self.oro = Oro(oro)
