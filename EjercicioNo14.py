"""
 Elabore un algoritmo que lea un número y obtenga su cuadrado y su cubo.
"""
class CalculadoraPotencias:
    def __init__(self, valor):
        self.numero = valor

    def cuadrado(self):
        return self.numero ** 2

    def cubo(self):
        return self.numero ** 3

    def mostrar_resultados(self):
        print(f"El cuadrado del numero {self.numero} es {self.cuadrado()}")
        print(f"Y su cubo es {self.cubo()}.")

n = int(input("Ingrese el numero: "))
operacion = CalculadoraPotencias(n)
operacion.mostrar_resultados()
