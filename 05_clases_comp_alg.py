"""
CLASES DE COMPLEJIDAD ALGORITMICA

· O(1) Constante
· O(n) Lineal
· O(log n) Logarítmica
· O(n log n) log lineal
· O(n²) Polinomial
· O(2ⁿ) Exponencial

"""

import math
import time


def num(n):
    return 1


def logarithm(n):
    return math.log10(n)


def lineal(n):
    return n


def n_logarithm(n):
    return n * math.log10(n)


def square(n):
    return n**2


def exponential(n):
    return 2**n


if __name__ == "__main__":
    n = [10, 100, 1000]

    for valor in n:
        print(f"{'=' * 60}")
        print(f"ANÁLISIS PARA n = {valor}")
        print(f"{'=' * 60}\n")

        # O(1) - Constante
        inicio = time.time()
        resultado = num(valor)
        fin = time.time()
        print("O(1) - Constante:")
        print(f"  Resultado: {resultado}")
        print(f"  Tiempo: {fin - inicio:.10f} segundos\n")

        # O(log n) - Logarítmica
        inicio = time.time()
        resultado = logarithm(valor)
        fin = time.time()
        print("O(log n) - Logarítmica:")
        print(f"  Resultado: {resultado:.4f}")
        print(f"  Tiempo: {fin - inicio:.10f} segundos\n")

        # O(n) - Lineal
        inicio = time.time()
        resultado = lineal(valor)
        fin = time.time()
        print("O(n) - Lineal:")
        print(f"  Resultado: {resultado}")
        print(f"  Tiempo: {fin - inicio:.10f} segundos\n")

        # O(n log n) - Log lineal
        inicio = time.time()
        resultado = n_logarithm(valor)
        fin = time.time()
        print("O(n log n) - Log lineal:")
        print(f"  Resultado: {resultado:.4f}")
        print(f"  Tiempo: {fin - inicio:.10f} segundos\n")

        # O(n²) - Polinomial
        inicio = time.time()
        resultado = square(valor)
        fin = time.time()
        print("O(n²) - Polinomial:")
        print(f"  Resultado: {resultado}")
        print(f"  Tiempo: {fin - inicio:.10f} segundos\n")

        # O(2ⁿ) - Exponencial
        if valor <= 100:  # Limitamos para evitar que tarde demasiado
            inicio = time.time()
            resultado = exponential(valor)
            fin = time.time()
            print("O(2ⁿ) - Exponencial:")
            print(f"  Resultado: {resultado}")
            print(f"  Tiempo: {fin - inicio:.10f} segundos\n")
        else:
            print("O(2ⁿ) - Exponencial:")
            print("  Resultado: [Demasiado grande para calcular]")
            print(f"  (2^{valor} = número con ~{int(valor * 0.301)} dígitos)\n")

        print("\n")
