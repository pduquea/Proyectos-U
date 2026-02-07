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

edad_juan = int(input("Ingrese la edad de Juan: "))
edad_alberto = (2/3) * edad_juan
edad_ana = (4/3) * edad_juan
edad_mama_juan = edad_juan + edad_alberto + edad_ana
print(f"Edades de los 3 hijos:\nJuan: {edad_juan}\nAlberto: {int(edad_alberto)}\nAna: {int(edad_ana)}\nEdad de la Mama de juan: {int(edad_mama_juan)}")

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
 
SUMA = 0
X = 20
SUMA = SUMA + X
Y = 40
X = X + Y ** 2
SUMA = SUMA + X / Y
print(f"EL VALOR DE LA SUMA ES: {SUMA}")

"""
Un empleado trabaja 48 horas en la semana a razón de $5.000 hora. El porcentaje de
retención en la fuente es del 12,5% del salario bruto. Se desea saber cuál es el salario bruto,
la retención en la fuente y el salario neto del trabajador.
"""

def retencion(monto):
    retenido = round((monto/100)*12.5)
    return retenido
Salario_bruto = 5000 * 48
Salario_neto = Salario_bruto - retencion(Salario_bruto)
retencion_fuente = retencion(Salario_bruto)
print(f"El salario del trabajor semanalmente será:\nSalario Bruto: {Salario_bruto}\nRetenido en la fuente: {retencion_fuente}\nSalario Neto: {Salario_neto}")

"""
 Elabore un algoritmo que lea un número y obtenga su cuadrado y su cubo.
"""

numero = int(input("Ingrese el numero para hallar su cuadrado y cubo: "))
print(f"El cuadrado del numero {numero} es {numero**2} y su cubo es {numero**3}.")

"""
Dado el radio de un círculo. Haga un algoritmo que obtenga el área del círculo y la longitud 
de la circunferencia.
"""

from math import pi

radio = int(input("Inserte el radio del circulo para calcular su area y circunferencia: "))
print(f"El area de circulo de radio {radio} es {round(pi*(radio**2), 2)} y su circunferencia es {round(2*radio*pi, 2)}")