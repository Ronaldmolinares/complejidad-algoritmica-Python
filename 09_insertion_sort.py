import random

# Ambos tienen complejidad O(n²) en el peor caso y O(n) en el mejor caso.


def insertion_sort(lista):
    n = len(lista)
    for indice in range(1, n):
        valor_actual = lista[indice]
        indice_elemento_anterior = indice - 1

        while (
            indice_elemento_anterior >= 0
            and lista[indice_elemento_anterior] > valor_actual
        ):
            lista[indice_elemento_anterior + 1] = lista[indice_elemento_anterior]
            indice_elemento_anterior -= 1

        lista[indice_elemento_anterior + 1] = valor_actual
    return lista


def ordenamiento_por_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista


if __name__ == "__main__":
    tamaño_lista = int(input("Tamaño de la lista: "))

    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]
    print(f"Lista original:\n{lista}")

    lista_ordenada = insertion_sort(lista)
    print(f"\nLista ordenada: {lista_ordenada}\n")
