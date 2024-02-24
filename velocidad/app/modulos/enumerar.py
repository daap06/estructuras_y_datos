from modulos.promedio import velocidad_promedio
from otros.datos import velocidad

def correas_sobre_promedio(velocidades):
    promedio = velocidad_promedio(velocidades)
    listado_correas = [i for i, v in enumerate(velocidad) if v > promedio]
    
    return listado_correas