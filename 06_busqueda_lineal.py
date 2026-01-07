import random


def busqueda_lineal(lista, busqueda):
    match = False
    for numero in lista:  # O(n)
        if busqueda == numero:
            match = True
            break

    return match


def busqueda_lineal_2(lista, busqueda):
    if busqueda in lista:
        return True
    return False


if __name__ == "__main__":
    tamaño_lista = int(input("Tamaño de la lista: "))
    busqueda = int(input("que numero va a encontrar"))

    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]

    encontrado = busqueda_lineal_2(lista, busqueda)
    print(lista)
    print(f"El elemento objetivo: {busqueda} {'está' if encontrado else 'no está'}")
