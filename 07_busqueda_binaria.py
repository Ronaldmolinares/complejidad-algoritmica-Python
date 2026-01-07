"""
BUSQUEDA BINARIA

- Divide y venceras
- El problema se divide en 2 en cada iteración
- ¿Cúal es el peor de los casos?
El peor de los casos ocurre cuando el elemento no está en la lista
o se encuentra en los extremos de la búsqueda. En esos escenarios,
el algoritmo debe agotar todas las divisiones posibles hasta que el rango sea vacío.
- Asume que la lista ya esta ordenada
"""

import random


def busqueda_binaria(lista, busqueda):
    bajo = 0
    alto = len(lista) - 1
    contador = 0

    while bajo <= alto:
        mitad = (bajo + alto) // 2
        indice = lista[mitad]
        contador += 1

        if indice == busqueda:
            print(f"Iteraciones busqueda binaria: {contador}.")
            return True

        if indice < busqueda:
            bajo = mitad + 1

        else:
            alto = mitad - 1

    print(f"Realizo {contador} iteraciones y no lo encontro.")
    return False


def busqueda_binaria_2(lista, comienzo, final, objetivo):
    if comienzo >= final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria_2(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria_2(lista, comienzo, medio - 1, objetivo)


if __name__ == "__main__":
    tamaño_lista = int(input("Tamaño de la lista: "))
    busqueda = int(input("que numero va a encontrar: "))

    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]
    lista.sort()

    encontrado = busqueda_binaria(lista, busqueda)
    # encontrado = busqueda_binaria_2(lista, 0, len(lista), busqueda)
    print(lista)
    print(f"El elemento objetivo: {busqueda} {'está' if encontrado else 'no está'}")
