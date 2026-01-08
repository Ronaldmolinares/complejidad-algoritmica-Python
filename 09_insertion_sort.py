import random


def insertion_sort(lista):
    n = len(lista)
    for indice in range(1, n):
        valor_actual = lista[indice]


if __name__ == "__main__":
    tamaño_lista = int(input("Tamaño de la lista: "))

    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]
    print(f"Lista original:\n{lista}")

    lista_ordenada = insertion_sort(lista)
    print(f"\nLista ordenada: {lista_ordenada}\n")
