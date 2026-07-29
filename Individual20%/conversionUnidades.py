class ConversionLongitud:
    def __init__(self, metros):
        self.metros = metros

    def a_centimetros(self):
        return self.metros * 100

    def a_milimetros(self):
        return self.metros * 1000

    def a_pulgadas(self):
        return self.metros * 39.3701

    def a_pies(self):
        return self.metros * 3.28084

    def a_yardas(self):
        return self.metros * 1.09361


class ConversionSuperficie:
    def __init__(self, metros_cuadrados):
        self.metros_cuadrados = metros_cuadrados

    def a_hectareas(self):
        return self.metros_cuadrados / 10000

    def a_kilometros_cuadrados(self):
        return self.metros_cuadrados / 1000000

    def a_fanegas(self):
        return self.metros_cuadrados / 6460

    def a_acres(self):
        return self.metros_cuadrados / 4046.85


class ConversionVolumen:
    def __init__(self, litros):
        self.litros = litros

    def a_galones(self):
        return self.litros / 4.41

    def a_pintas(self):
        return self.litros / 0.46

    def a_bariles(self):
        return self.litros / 158.99

    def a_metros_cubicos(self):
        return self.litros / 1000

    def a_hectolitros(self):
        return self.litros / 100


def main():
    metros = float(input("Ingrese la cantidad en metros para longitud: "))
    metros_cuadrados = float(input("Ingrese la cantidad en metros cuadrados para superficie: "))
    litros = float(input("Ingrese la cantidad en litros para volumen: "))

    longitud = ConversionLongitud(metros)
    superficie = ConversionSuperficie(metros_cuadrados)
    volumen = ConversionVolumen(litros)

    print("\nResultados")
    print("Longitud")
    print(f"Centímetros: {longitud.a_centimetros():.2f}")
    print(f"Milímetros: {longitud.a_milimetros():.2f}")
    print(f"Pulgadas: {longitud.a_pulgadas():.2f}")
    print(f"Pies: {longitud.a_pies():.2f}")
    print(f"Yardas: {longitud.a_yardas():.2f}")

    print("\nSuperficie")
    print(f"Hectáreas: {superficie.a_hectareas():.6f}")
    print(f"Kilómetros cuadrados: {superficie.a_kilometros_cuadrados():.8f}")
    print(f"Fanegas: {superficie.a_fanegas():.6f}")
    print(f"Acres: {superficie.a_acres():.6f}")

    print("\nVolumen")
    print(f"Galones: {volumen.a_galones():.4f}")
    print(f"Pintas: {volumen.a_pintas():.4f}")
    print(f"Barriles: {volumen.a_bariles():.4f}")
    print(f"Metros cúbicos: {volumen.a_metros_cubicos():.4f}")
    print(f"Hectolitros: {volumen.a_hectolitros():.4f}")


if __name__ == "__main__":
    main()
