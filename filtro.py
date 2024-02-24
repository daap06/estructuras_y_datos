import sys

precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

#Función para manejar errores.
def valida_datos(argumentos):
    try: 
        if len(argumentos) < 2:
            raise ValueError("Falta un parámetro, por favor verifique.")
        if argumentos[1].isdigit() != True:
            raise ValueError("Ingrese valor numérico")
        if len(argumentos) == 3:
            if argumentos[2] not in ["menor", "mayor"]:
                raise ValueError("Lo sentimos, no es una operación válida")
    except ValueError as e:
        print(e)
        return False #Retorna False en caso de que el flujo presente problemas.
    
    return True #Retorna True si el flujo se completa sin errores.

argumento = sys.argv  

def print_resultado(parametro1, parametro2):
    print(f"los productos {parametro1}es al umbral son:",', '.join(parametro2))

# Función para ejecutar el filtro considerando diferentes criterios.

def filtro_resultado(argumento):        
    prueba = int(argumento[1] )
    if len(argumento) == 3: # Con tres parámetros
        filtro_dinamico = {k: v for k,v in precios.items() if (v < prueba and argumento[2] == "menor") or (v > prueba and argumento[2] == "mayor")}
        print_resultado(argumento[2],filtro_dinamico)
    else: # Con dos parámetros
        filtro_dinamico = {k: v for k,v in precios.items() if (v > prueba)}
        print_resultado("mayores",filtro_dinamico)
        
# Si la función valida_datos retorna True se ejecuta la segunda función, llamo la función con main.       

def main():
    if valida_datos(argumento) is True:
        filtro_resultado(argumento)     
        
if __name__ == '__main__':
    main()

    
    





    
