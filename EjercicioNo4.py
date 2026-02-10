"""
Ejercicio resuelto No 4
A la mamá de Juan le preguntan su edad, y contesta: tengo 3 hijos, pregúntele a Juan su
edad. Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la edad de Juan y mi edad es
la suma de las tres. Hacer un algoritmo que muestre la edad de los cuatro.
Análisis
Es necesario que al algoritmo se le proporcione la edad de Juan para calcular la edad de
Alberto, de Ana y de la mamá.
Datos de entrada
    • Edad de Juan.
Datos de salida
    • Edad de Alberto.
    • Edad de Juan. (En este caso es un dato de entrada y salida al mismo tiempo).
    • Edad de Ana.
    • Edad de la mamá.
Proceso
    • Edad de Alberto = 2/3 * edad de Juan.
    • Edad de Ana = 4/3 * edad de Juan.
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = int(edad)

class CalculadorFamilia:
    def __init__(self, edad_juan):

        self.juan = Persona("Juan", edad_juan)
        self.alberto = Persona("Alberto", (2/3) * edad_juan)
        self.ana = Persona("Ana", (4/3) * edad_juan)
        
        edad_mama = self.juan.edad + self.alberto.edad + self.ana.edad
        self.mama = Persona("Mamá de Juan", edad_mama)

    def mostrar_reporte(self):
        print("--- Reporte de Edades ---")
        for hijo in [self.juan, self.alberto, self.ana]:
            print(f"{hijo.nombre}: {hijo.edad} años")
        print(f"-------------------------")
        print(f"{self.mama.nombre}: {self.mama.edad} años")

edad_input = int(input("Ingrese la edad de Juan: "))
familia = CalculadorFamilia(edad_input)
familia.mostrar_reporte()