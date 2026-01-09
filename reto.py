if __name__ == "__main__":
    numero = int(input("determinar la cantidad de digitos: "))
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

    # if numero / 10 < 1:
    #     print(f"el numero {numero} tiene 1 digito")
    # elif numero / 10 < 10:
    #     print(f"el numero {numero} tiene 2 digitos")
    # elif numero / 10 < 100:
    #     print(f"el numero {numero} tiene 3 digitos")
    # else:
    #     print("el numero tiene mas de 3 digitos")
