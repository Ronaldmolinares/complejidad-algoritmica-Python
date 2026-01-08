import random


def burbuja(lista):  # Complejidad O(n²)
    n = len(lista)
    intercambios = 0
    for pasada in range(n):
        for j in range(0, n - pasada - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    return lista, intercambios


if __name__ == "__main__":
    tamaño_lista = int(input("Tamaño de la lista: "))

    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]
    print(f"Lista original:\n{lista}")

    lista_ordenada, intercambios = burbuja(lista)
    print(f"\nLista ordenada: {lista_ordenada}\nNúmero de intercambios: {intercambios}")
