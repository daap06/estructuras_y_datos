from modulos.factorial import calculo_factorial
from modulos.productoria import calculo_productoria

resultados = []
#Función para controlar calculos realizados.
def control_calculos(**kwargs):
    for clave, valor in kwargs.items():
        if 'fact_' in clave:
            resultado = calculo_factorial(valor)
            resultados.append(f"El factorial de {valor} es {resultado}")
        elif 'prod_' in clave:
            resultado = calculo_productoria(valor)
            resultados.append(f"La productoria de {valor} es {resultado}")
    return resultados