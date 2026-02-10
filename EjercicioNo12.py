
"""
Un empleado trabaja 48 horas en la semana a razón de $5.000 hora. El porcentaje de
retención en la fuente es del 12,5% del salario bruto. Se desea saber cuál es el salario bruto,
la retención en la fuente y el salario neto del trabajador.
"""

class Nomina:
    def __init__(self, pago_por_hora, horas_totales):
        self.salario_bruto = pago_por_hora * horas_totales
        self.tasa_retencion = 12.5

    def calcular_retencion(self):
        return round((self.salario_bruto / 100) * self.tasa_retencion)

    def obtener_neto(self):
        return self.salario_bruto - self.calcular_retencion()

    def imprimir_recibo(self):
        print(f"--- Recibo de Pago ---")
        print(f"Salario Bruto: {self.salario_bruto}")
        print(f"Retención ({self.tasa_retencion}%): {self.calcular_retencion()}")
        print(f"Salario Neto: {self.obtener_neto()}")

# Uso de la clase
empleado1 = Nomina(5000, 48)
empleado1.imprimir_recibo()