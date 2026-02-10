
"""
Dado el radio de un círculo. Haga un algoritmo que obtenga el área del círculo y la longitud 
de la circunferencia.
"""

from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return round(pi * (self.radio ** 2), 2)

    def calcular_circunferencia(self):
        return round(2 * pi * self.radio, 2)

r = int(input("Inserte el radio del circulo: "))
mi_circulo = Circulo(r)

print(f"El área es: {mi_circulo.calcular_area()}")
print(f"La circunferencia es: {mi_circulo.calcular_circunferencia()}")