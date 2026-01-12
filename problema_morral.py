import random

"""
PROBLEMA DEL MORRAL

Escoger cual de los articulos me va a otorgar el mayor valor posible.
Se trata de: algoritmo 0-1 Knapsack Problem, aca no se pueden subdivir los
elementos, o los tomas por completo o los dejas.
Se le da solución con una funcion recursiva.

"""


def morral(tamano_morral, pesos, valores, n):
    # Caso base 1: Si ya no nos quedan mas elementos o si ya no hay espacio en el morral
    if n == 0 or tamano_morral == 0:
        return 0

    # Caso base 2: Si el elemento que quiero incluir pesa mas que el morral
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    # Ahora viene la desición de si tomar o no el elemento
    # TOMO el elemento (1): Escojo el valor del elemento actual y le quito al tamaño de mi morral lo que pesa ese elemento
    return max(
        valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
        # en el caso de que no lo tomo (0)
        morral(tamano_morral, pesos, valores, n - 1),
    )


if __name__ == "__main__":
    numero_elementos = int(input("Numero de elementos: "))
    valores = [
        random.randint(60, 121) for _ in range(numero_elementos)
    ]  # cuanto vale cada elemento
    print(f"Valores de los {numero_elementos} elementos: {valores} ")

    pesos = [
        random.randint(10, 31) for _ in range(numero_elementos)
    ]  # cuanto pesa cada elemento
    print(f"Pesos de los {numero_elementos} elementos: {pesos} \n")

    tamano_morral = 50  # la capacidad
    n = len(
        valores
    )  # indice sobre el que vamos a estar trabajando (empieza en el final)

    resultado = morral(tamano_morral, pesos, valores, n)

    print(
        f"El valor maximo que se puede llevar con un tamaño de mochila de {tamano_morral} es de: {resultado}"
    )
