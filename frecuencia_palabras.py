def color_frecuente(lista):
    #lista2 = []
    lista3 = []
    for i in lista:
        x = lista.count(i)
        #lista2.append([i,x]) 
        lista3.append([x,i]) # [numero,"color"]
        lista3.sort()
    maximo = lista3[-1][0]
    #print(maximo)

    if ([maximo,"azul"] in lista3):
        resultado = ("azul",maximo)
    elif ([maximo,"rojo"] in lista3):
        resultado = ("rojo",maximo)
    elif ([maximo,"verde"] in lista3):
        resultado = ("verde",maximo)
    elif ([maximo,"amarillo"] in lista3):
        resultado = ("amarillo",maximo)

    return resultado
	
"""
Suponga que tiene una lista de colores repetidos y desordenados, estos pueden ser: azul, rojo, verde y amarillo. Desea saber cual de esos colores es el que más se repite. Escriba una función color_frecuente que reciba como argumento a una lista de strings llamada lista y retorne el string más repetido y el número de ocurrencias del mismo.
Por ejemplo para la lista ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
Debe retornar: "verde", 8
En caso de que haya varios colores con el máximo número, se retornará con la siguiente prioridad: azul, rojo, verde, amarillo. Es decir, por ejemplo si la lista es l = ['rojo', 'rojo', 'azul', azul'], la función debe retornar "azul", 2
"""