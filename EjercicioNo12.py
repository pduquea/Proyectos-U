
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