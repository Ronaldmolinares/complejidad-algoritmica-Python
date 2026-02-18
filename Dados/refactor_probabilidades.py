import random


def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros


def tirar_dos_dados(numero_de_tiros):
    """Tira dos dados 'numero_de_tiros' veces y retorna lista de sumas.

    Args:
        numero_de_tiros: Cuántas veces tirar ambos dados

    Returns:
        Lista con las sumas de cada par de tiros
        Ejemplo: [7, 3, 11, 6] significa (3+4), (1+2), (5+6), (4+2)
    """
    sumas = []
    for _ in range(numero_de_tiros):
        dado_1 = random.choice([1, 2, 3, 4, 5, 6])
        dado_2 = random.choice([1, 2, 3, 4, 5, 6])
        suma = dado_1 + dado_2
        sumas.append(suma)

    return sumas


def main2(numero_de_tiros, numero_de_intentos, objetivo):
    """Simula lanzar dos dados y cuenta cuántas veces la suma es igual al objetivo.

    Args:
        numero_de_tiros: Cuántos pares de dados tirar en cada intento
        numero_de_intentos: Cuántas veces repetir la simulación
        objetivo: Suma objetivo a buscar (2-12)
    """
    todas_las_sumas = []  # Guardará TODAS las sumas de todos los intentos

    # Repetir la simulación 'numero_de_intentos' veces
    for _ in range(numero_de_intentos):
        sumas_de_este_intento = tirar_dos_dados(numero_de_tiros)
        todas_las_sumas.extend(sumas_de_este_intento)  # Agregar todas las sumas

    # Contar cuántas veces apareció el objetivo
    veces_que_salio_objetivo = todas_las_sumas.count(objetivo)

    # Total de tiros realizados
    total_de_tiros = numero_de_tiros * numero_de_intentos

    # Calcular probabilidad experimental
    probabilidad_objetivo = veces_que_salio_objetivo / total_de_tiros

    # Mostrar resultados
    print(f"\n{'=' * 70}")
    print(f"SIMULACIÓN: Probabilidad de obtener suma = {objetivo}")
    print(f"{'=' * 70}")
    print(f"Número de tiros por intento: {numero_de_tiros}")
    print(f"Número de intentos: {numero_de_intentos}")
    print(f"Total de tiros realizados: {total_de_tiros}")
    print(f"Veces que salió {objetivo}: {veces_que_salio_objetivo}")
    print(
        f"Probabilidad experimental: {probabilidad_objetivo:.4f} ({probabilidad_objetivo * 100:.2f}%)"
    )
    print(f"{'=' * 70}\n")

    # Calcular probabilidad teórica para comparar
    probabilidades_teoricas = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }
    prob_teorica = probabilidades_teoricas.get(objetivo, 0)
    print(
        f"Probabilidad teórica para suma={objetivo}: {prob_teorica:.4f} ({prob_teorica * 100:.2f}%)"
    )
    print(f"Diferencia: {abs(probabilidad_objetivo - prob_teorica):.4f}\n")


def main(numero_de_tiros, numero_de_intentos):
    tiros = []  # se guardan los resultados de la simulación

    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_1 = 0
    for tiro in tiros:
        # if 1 not in tiro:
        if 1 in tiro:
            tiros_con_1 += 1

    print(tiros)

    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(
        f"Probabilidad de obtener por lo menos un 1 lanzando {numero_de_tiros} veces el dado en {numero_de_intentos} intentos es de: {probabilidad_tiros_con_1}"
        # f"Probabilidad de NO obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}"
    )


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("SIMULADOR DE PROBABILIDADES CON DADOS")
    print("=" * 70)

    print("\n¿Qué simulación quieres ejecutar?")
    print("1) Probabilidad de obtener al menos un 1 en N tiros (un solo dado)")
    print("2) Probabilidad de obtener una suma específica (dos dados)")

    opcion = input("\nElige una opción (1 o 2): ")

    numero_de_tiros = int(
        input("¿Cuántas veces lanzar el/los dado(s) en cada intento? ")
    )
    numero_de_intentos = int(input("¿Cuántas veces repetir la simulación? "))

    if opcion == "1":
        main(numero_de_tiros, numero_de_intentos)
    elif opcion == "2":
        objetivo = int(input("¿Qué suma objetivo buscas? (2-12): "))
        main2(numero_de_tiros, numero_de_intentos, objetivo)
    else:
        print("Opción inválida")
