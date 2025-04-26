from .Soldados import Soldado

class Jinete(Soldado):
    def __init__(self):
        super().__init__("Horseman", comida=140, madera=0, oro=100, poder=230)
