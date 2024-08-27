def gerarsequenciasvalidasrecursiva(listadesequencias, lista, nivel, nivelmax, epislonGlobal):
    if sum(lista) > epislonGlobal:
        return
    if nivel == nivelmax and sum(lista) != epislonGlobal:
        return
    if nivel == nivelmax and sum(lista) == epislonGlobal:
        listadesequencias.append(lista)
        return
    for i in range(1,50):
        listatemp = list(lista)
        listatemp.append(0.020*i)
        gerarsequenciasvalidasrecursiva(listadesequencias, listatemp, nivel+1, nivelmax, epislonGlobal)
    return


lis = []
gerarsequenciasvalidasrecursiva(lis, [], 0, 6, 1.0)
print(lis)
print(len(lis))
