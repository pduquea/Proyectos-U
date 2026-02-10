
"""
Hacer un seguimiento (prueba de escritorio) del siguiente grupo de instrucciones.
INICIO
SUMA = 0
X = 20
SUMA = SUMA + X
Y = 40
X = X + Y ** 2
SUMA = SUMA + X / Y
ESCRIBA: “EL VALOR DE LA SUMA ES:”, SUMA
FIN_INICIO
"""
 
class Calculadora:
    def __init__(self, x_inicial, y_inicial):
        self.suma = 0
        self.x = x_inicial
        self.y = y_inicial

    def ejecutar_operaciones(self):
        self.suma += self.x
        
        self.x = self.x + self.y ** 2
        
        self.suma += self.x / self.y

    def mostrar_resultado(self):
        print(f"EL VALOR DE LA SUMA ES: {self.suma}")

mi_operacion = Calculadora(20, 40)
mi_operacion.ejecutar_operaciones()
mi_operacion.mostrar_resultado()