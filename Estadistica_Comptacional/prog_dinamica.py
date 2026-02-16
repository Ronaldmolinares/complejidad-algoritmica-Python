def fibonacci(num):
    a = 0
    b = 1

    for _ in range(num + 1):
        a, b = b, a + b

    return a


def fibonacci_recursivo(num):
    if num == 0 or num == 1:
        return 1

    return fibonacci_recursivo(num - 1) + fibonacci_recursivo(num - 2)


def fibonacci_dinamico(num: int, memo=None):
    if num == 0 or num == 1:
        return 1
    memo = {}
    try:
        return memo[num]
    except KeyError:
        result = fibonacci_dinamico(num - 1, memo) + fibonacci_dinamico(num - 2, memo)
        memo[num] = result

        return result


if __name__ == "__main__":
    valor = int(input("Numero de Fibonacci: "))

    fibo_Tradicional = fibonacci(valor)
    print(fibo_Tradicional)

    fibo_Recursivo = fibonacci_recursivo(valor)
    print(fibo_Recursivo)

    fibo_Dinamico = fibonacci_dinamico(valor)
    print(fibo_Dinamico)
