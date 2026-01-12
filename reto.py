import random


def ordenamiento_mezcla(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        i = 0
        j = 0
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
                k += 1
            else:
                lista[k] = derecha[j]
                j += 1
                k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista


def numero_mayor(lista):
    resultado = lista[0]

    for numero in lista:
        if numero > resultado:
            resultado = numero

    return resultado


if __name__ == "__main__":
    numero = int(input("Determinar la cantidad de dígitos de un número: "))
    valor = numero
    contador = 0
    if numero == 0:
        contador = 1

    while numero > 0:
        contador += 1
        numero = numero // 10

    print(
        f"El número {valor} tiene {contador} {'digito.' if contador == 1 else 'dígitos.'}"
    )

    tamaño_lista = int(input("Tamaño de la lista: "))

    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]
    print(f"Lista original:\n{lista}")

    resultado = numero_mayor(lista)
    print(f"\nNumero mayor: {resultado}\n")

    # if numero / 10 < 1:
#     print(f"el numero {numero} tiene 1 digito")
# elif numero / 10 < 10:
#     print(f"el numero {numero} tiene 2 digitos")
# elif numero / 10 < 100:
#     print(f"el numero {numero} tiene 3 digitos")
# else:
#     print("el numero tiene mas de 3 digitos")
