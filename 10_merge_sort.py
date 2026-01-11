import random

"""
Complejidad del algoritmo: O(n log n)

- La lista se divide en mitades recursivamente, lo que genera 'log n' niveles de recursión.
En cada nivel, se recorren todos los 'n' elementos para combinarlos.
De manera que: log n niveles x n operaciones por nivel = O(n log n)

Ventajas
- Complejidad temporal O(n log n) en todos los casos
- Mantiene el orden relativo de elementos iguales
- Eficiente para listas grandes

Desventajas
- Requiere espacio adicional O(n)
- No es "in-place" como Quick Sort puede serlo
"""


def merge_sort(lista):
    # Caso base de la recursión:  lista con 1 o 0 elementos ya está ordenada por definición.
    if len(lista) > 1:
        # Dividir la lista en dos mitades
        mitad = (len(lista)) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        # Llamada recursiva en cada mitad
        # Se va a ejecutar hasta que quede 1 elemento en la lista
        merge_sort(izquierda)
        merge_sort(derecha)

        # Iteradores para recorrer las sublistas
        i = 0  # Iterador de la lista izquierda
        j = 0  # Iterador de la lista derecha
        k = 0  # Iterador para la lista principal

        while i < len(izquierda) and j < len(
            derecha
        ):  # Mientras podamos seguir comparando
            # Revisamos cual es el mayor y cual es el menor para irlo colocando
            # en la posición del indice k --> lista ordenada
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        # Ahora vaciamos los elementos que queden en alguna de las sublistas (izquierda, derecha)

        # Se ejecuta si la lista derecha ya no tiene elementos, copiando la lista
        # izquierda al final de la lista principal porque ya esta ordenada
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Se ejecuta si la lista izquierda ya no tiene elementos, copiando la lista
        # derecha al final de la lista principal
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista


if __name__ == "__main__":
    print("::::::::ORDENAMIENTO POR MEZCLA::::::::")
    tamaño_lista = int(input("Tamaño de la lista: "))

    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]
    print(f"Lista original:\n{lista}")

    lista_ordenada = merge_sort(lista)
    print(f"\nLista ordenada:\n{lista_ordenada}\n")
