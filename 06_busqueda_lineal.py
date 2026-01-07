import random


def busqueda_lineal(lista, busqueda):
    match = False
    contador = 0
    for numero in lista:  # O(n)
        contador += 1
        if busqueda == numero:
            match = True
            print(f"Iteraciones busqueda lineal: {contador}.")
            break

    if not match:
        print(f"Realizo {contador} iteraciones y no lo encontro.")

    return match


def busqueda_lineal_2(lista, busqueda):
    if busqueda in lista:
        return True
    return False


if __name__ == "__main__":
    tamaño_lista = int(input("Tamaño de la lista: "))
    busqueda = int(input("que numero va a encontrar: "))

    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]

    encontrado = busqueda_lineal(lista, busqueda)
    print(lista)
    print(f"El elemento objetivo: {busqueda} {'está' if encontrado else 'no está'}")
