class Profesor:
    def imprimir(self):
        print("Profesor")


class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Profesor Titular")


def main():
    profesor1 = ProfesorTitular()
    profesor2 = profesor1
    profesor2.imprimir()


if __name__ == "__main__":
    main()

# Se puede observar que el método imprimir() de la clase ProfesorTitular 
# sobrescribe el método imprimir() de la clase Profesor. Por lo tanto,
# cuando se llama al método imprimir() a través de la referencia profesor2,
# se ejecuta el método de la clase ProfesorTitular, mostrando "Profesor Titular"
