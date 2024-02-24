from modulos.valida_datos import valida_datos
from modulos.filtros import filtro_resultado
import sys

argumento = sys.argv  
def main():
        if valida_datos(argumento) is True:
            filtro_resultado(argumento)  

if __name__ == '__main__':
    main()