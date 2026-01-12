import random

"""
PROBLEMA DEL MORRAL

Escoger cual de los articulos me va a otorgar el mayor valor posible.
Se trata de: 0-1 Knapsack Problem, aca no se pueden subdivir los
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


def morral_verbose(tamano_morral, pesos, valores, n, nivel=0):
    indent = "  " * nivel  # Indentación para visualizar niveles

    # Caso base 1
    if n == 0 or tamano_morral == 0:
        print(f"{indent}🛑 FIN: No quedan elementos o capacidad → Retorna: 0")
        return 0, []  # retorna valor y lista vacía de elementos

    elemento_actual = n - 1  # Índice del elemento actual en el array

    print(f"\n{indent}{'=' * 50}")
    print(f"{indent}📦 Considerando {n} elementos | Capacidad: {tamano_morral}")
    print(
        f"{indent}   Evaluando Elemento indice #{elemento_actual}: valor={valores[elemento_actual]}, peso={pesos[elemento_actual]}"
    )

    # Caso base 2
    if pesos[elemento_actual] > tamano_morral:
        print(
            f"{indent}❌ NO cabe (peso {pesos[elemento_actual]} > capacidad {tamano_morral})"
        )
        print(f"{indent}   Saltando al siguiente...")
        return morral_verbose(tamano_morral, pesos, valores, n - 1, nivel + 1)

    # Decisión
    print(f"{indent}   🔍 Probando ambas opciones:")

    print(
        f"{indent}      [A] SI tomar elemento #{elemento_actual} → capacidad restante: {tamano_morral - pesos[elemento_actual]}"
    )
    valor_tomar, elementos_tomar = morral_verbose(
        tamano_morral - pesos[elemento_actual], pesos, valores, n - 1, nivel + 1
    )
    valor_tomar += valores[elemento_actual]
    elementos_tomar = [elemento_actual] + elementos_tomar

    print(
        f"{indent}      [B] NO tomar elemento #{elemento_actual} → capacidad: {tamano_morral}"
    )
    valor_no_tomar, elementos_no_tomar = morral_verbose(
        tamano_morral, pesos, valores, n - 1, nivel + 1
    )

    if valor_tomar > valor_no_tomar:
        print(
            f"{indent}✅ Elemento #{elemento_actual}: SI={valor_tomar} vs NO={valor_no_tomar} → Mejor: {valor_tomar}"
        )
        return valor_tomar, elementos_tomar
    else:
        print(
            f"{indent}✅ Elemento #{elemento_actual}: SI={valor_tomar} vs NO={valor_no_tomar} → Mejor: {valor_no_tomar}"
        )
        return valor_no_tomar, elementos_no_tomar


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

    valor_max, elementos_seleccionados = morral_verbose(
        tamano_morral, pesos, valores, n
    )

    print("\n" + "=" * 60)
    print("🎒 RESULTADO FINAL:")
    print(f"   Valor máximo: {valor_max}")
    print(
        f"   Capacidad usada: {sum(pesos[i] for i in elementos_seleccionados)}/{tamano_morral}"
    )
    print("\n   📦 Elementos seleccionados:")
    for elem in elementos_seleccionados:
        print(f"      - Elemento #{elem}: valor={valores[elem]}, peso={pesos[elem]}")
    print("=" * 60)
