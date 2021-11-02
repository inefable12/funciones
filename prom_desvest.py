def promedio_std(lista):
    u = 0
    sum2 = 0
    for i in lista:
        u = u + i
    x = u/len(lista)
    for j in lista:
        sum2 = sum2 + (j-x)**2
    y = ((sum2 / len(lista)))**0.5
    return (x,y)