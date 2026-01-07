# Ley de la suma


def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)


# 0(n) + 0(n)=0(n+n)=0(2n)=0(n)


# Ley de la suma


def g(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)


# 0(n) + 0(n * n) = 0(n +n²)=0(n²)


# Ley de la multiplicación


def h(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# 0(n) * 0(n)=0(n*n)=0(n²)


# Recursividad Múltiple
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# O(2ⁿ)
