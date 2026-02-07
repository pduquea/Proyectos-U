
"""
Dado el radio de un círculo. Haga un algoritmo que obtenga el área del círculo y la longitud 
de la circunferencia.
"""

from math import pi

radio = int(input("Inserte el radio del circulo para calcular su area y circunferencia: "))
print(f"El area de circulo de radio {radio} es {round(pi*(radio**2), 2)} y su circunferencia es {round(2*radio*pi, 2)}")