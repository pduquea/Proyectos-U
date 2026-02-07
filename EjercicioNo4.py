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