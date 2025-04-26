from .Soldados import Soldado

class Espadachin(Soldado):
    def __init__(self):
        super().__init__("Swordsman", comida=60, madera=20, oro=0, poder=70)
