"""
Ejemplo de métodos polimórficos (adaptado del enunciado).

Salida esperada al ejecutar el programa:
Profesor
Profesor Titular

se crea un vector/lista que contiene un objeto `Profesor` y
otro objeto `ProfesorTitular`. Al iterar y llamar a `imprimir()` se ejecuta
la implementación correspondiente a cada objeto (comportamiento polimórfico).
"""

class Profesor:
    def imprimir(self):
        print("Profesor")


class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Profesor Titular")


def main():
    # Simula el Vector del enunciado usando una lista de Python
    profesores = []

    profesor1 = Profesor()
    profesor2 = ProfesorTitular()

    profesores.append(profesor1)
    profesores.append(profesor2)

    # Iterar y llamar al método imprimir() muestra comportamiento polimórfico
    for p in profesores:
        p.imprimir()


if __name__ == "__main__":
    main()
