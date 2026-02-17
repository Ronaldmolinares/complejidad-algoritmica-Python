from Estadistica_Comptacional.borracho import BorrachoTradicional
from Estadistica_Comptacional.campo import Campo
from Estadistica_Comptacional.coordenada import Coordenada


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho(nombre="Juan")
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_intentos):
        campo = Campo()
        campo.add_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def main(distancia_caminata, numero_intentos, tipo_borracho):

    for pasos in distancia_caminata:
        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_max = max(distancias)
        distancia_min = min(distancias)

        print(f"{tipo_borracho.__name__} caminata aleatoria de {pasos} pasos")
        print(
            f" Media = {distancia_media}\n Max = {distancia_max}\n Min = {distancia_min}"
        )


if __name__ == "__main__":
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_intentos = 100

    main(distancias_de_caminata, numero_intentos, BorrachoTradicional)
