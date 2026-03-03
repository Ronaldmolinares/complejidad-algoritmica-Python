import collections
import random

PALOS = {"espada", "corazon", "diamante", "trebol"}
VALORES = {"as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jota", "reina", "rey"}


def crear_baraja():
    barajas = []

    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas


def obtener_mano(barajas, numero_de_cartas):
    mano = random.sample(barajas, numero_de_cartas)

    return mano


def main(mano, intentos):
    barajas = crear_baraja()
    manos_obtenidas = []

    for _ in range(intentos):
        mano_obtenida = obtener_mano(barajas, mano)
        manos_obtenidas.append(mano_obtenida)

    pares = 0

    for mano in manos_obtenidas:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for valor in counter.values():
            if valor == 2:
                pares += 1
                break

        probabilidades_par = pares / intentos
    print(f"\n{'=' * 70}")
    print(
        f"La probabilidad de obtener un par en una mano de {mano} cartas es de: {probabilidades_par:.4f} ({probabilidades_par * 100:.2f}%)"
    )
    print(f"{'=' * 70}")


if __name__ == "__main__":
    tamano_mano = int(input("Ingrese el número de cartas en la mano: "))
    intentos = int(input("Ingrese el número de intentos para obtener la mano: "))

    main(tamano_mano, intentos)
