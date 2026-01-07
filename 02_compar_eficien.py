import sys
import time

# Se Aumenta el límite de recursión para permitir cálculos más grandes
sys.setrecursionlimit(2000)


def factorial_tradicional(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_recursivo(numero):
    if numero > 1:
        return numero * factorial_recursivo(numero - 1)
    else:
        return 1


resultado = factorial_recursivo(2)
print(resultado)


def fibonacci(numero):
    if numero == 1:
        return 1
    elif numero == 0:
        return 0
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


def fibonacci_tradicional(numero):
    a = 0
    b = 1
    for i in range(numero):
        a, b = b, a + b
    return a


valor = fibonacci_tradicional(7)
print(valor)

if __name__ == "__main__":
    n = 1200

    comienzo = time.time()
    factorial_tradicional(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_recursivo(n)
    final = time.time()
    print(final - comienzo)
