from modulos.calculos import control_calculos

def main():
    resultados = control_calculos(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)
    for resultado in resultados:
        print(resultado)
    
if __name__ == "__main__":
    main()