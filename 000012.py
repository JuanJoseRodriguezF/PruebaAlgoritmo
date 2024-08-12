# 1. Leer el numero de casos n
# 2. leer de 2 en 2 los arreglos para evaluar
# 3. Evaluamos estos dos arreglos para que se nos devuelvan los elementos repetidos
def interListas(lista1, lista2):
    # 1. verificar lista mas corta
    # 2. Iterar sobre esa lista
    # 2.1 Comparo el elemento si esta dentro de la otra lista
    listaATrabajar = lista2
    listaAComparar = lista1
    if len(lista1) < len(lista2):
        listaATrabajar = lista1
        listaAComparar = lista2

    # forma 1
    # for i in range (len(listaATrabajar)):
    #    listaATrabajar[i]

    # forma 2
    resultado = list()
    for entero in listaATrabajar:
        if entero in listaAComparar:
            resultado.append(entero)

    return resultado

def interSet(lista1, lista2):
    return lista1.intersection(lista2)

def main():
    n = int(input())
    for _ in range(n):
        lista1 = set(input().split(" ")) # 1 1 1 1
        lista2 = set(input().split(" ")) # 1 1 1 1
        resultado = interSet(lista1, lista2)
        if len(resultado) == 0:
            print("No hay elementos")
        else:
            print(" ".join(map(str, resultado)))
main()