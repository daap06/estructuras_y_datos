#Función para calcular productoria de una lista de números
def calculo_productoria(lista):
    productoria = 1
    for i in lista:
        productoria *= i
    return productoria