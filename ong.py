#Función para calcular factorial de un número
def calculo_factorial(n):
    if n == 0 or n ==1:
        return 1
    elif n > 1:
        factorial = n * calculo_factorial(n-1) 
    return factorial
        

#Función para calcular productoria de una lista de números
def calculo_productoria(lista):
    productoria = 1
    for i in lista:
        productoria *= i
    return productoria


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
            
def main():
    resultados = control_calculos(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)
    for resultado in resultados:
        print(resultado)
    
if __name__ == "__main__":
    main()
