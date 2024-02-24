import sys 
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
