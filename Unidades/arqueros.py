from .Soldados import Soldado

class Arquero(Soldado):
    def __init__(self):
        super().__init__("Bowman", comida=80, madera=10, oro=40, poder=95)
