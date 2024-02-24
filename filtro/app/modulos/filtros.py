from modulos.mostrar_resultados import print_resultado

precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

def filtro_resultado(argumento):        
    prueba = int(argumento[1] )
    if len(argumento) == 3: # Con tres parámetros
        filtro_dinamico = {k: v for k,v in precios.items() if (v < prueba and argumento[2] == "menor") or (v > prueba and argumento[2] == "mayor")}
        print_resultado(argumento[2],filtro_dinamico)
    else: # Con dos parámetros
        filtro_dinamico = {k: v for k,v in precios.items() if (v > prueba)}
        print_resultado("mayores",filtro_dinamico)