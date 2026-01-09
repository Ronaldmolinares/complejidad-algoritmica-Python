import random


def merge_sort(lista):
    pass


if __name__ == "__main__":
    tamaño_lista = int(input("Tamaño de la lista: "))

    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]
    print(f"Lista original:\n{lista}")

    lista_ordenada = merge_sort(lista)
    print(f"\nLista ordenada: {lista_ordenada}\n")
