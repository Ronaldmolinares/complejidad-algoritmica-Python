from bokeh.plotting import figure, show
from borracho import BorrachoContinuo, BorrachoTradicional
from campo import Campo
from coordenada import Coordenada


def caminata(campo, borracho, pasos):
    """Guarda la posición inicial"""
    inicio = campo.obtener_coordenada(borracho)
    """Ejecuta N pasos aleatorios"""
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    """Retorna: Un float con la distancia final desde el origen"""
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

    """Retorna: Una lista de floats con todas las distancias finales"""
    return distancias


def graficar(array_x, datos_por_tipo):
    """Visualización de la caminata aleatoria comparando diferentes tipos de borracho.

    Args:
        array_x: Cantidad de pasos que da el borracho
        datos_por_tipo: Diccionario {nombre_tipo: [distancias_medias]}
    """
    grafica = figure(
        title="Comparación de Caminos Aleatorios",
        x_axis_label="Pasos",
        y_axis_label="Distancia Media",
    )

    colores = ["blue", "red", "green", "orange"]
    for i, (nombre_tipo, array_y) in enumerate(datos_por_tipo.items()):
        grafica.line(
            array_x,
            array_y,
            legend_label=nombre_tipo,
            line_width=2,
            color=colores[i % len(colores)],
        )

    grafica.legend.click_policy = "hide"  # Permite ocultar líneas al hacer clic
    show(grafica)


def main(distancia_caminata, numero_intentos, tipos_borracho):
    """Ejecuta simulaciones para múltiples tipos de borracho y los compara.

    Args:
        distancia_caminata: Lista de cantidades de pasos a probar
        numero_intentos: Cuántas veces repetir cada experimento
        tipos_borracho: Lista de clases de borracho a comparar
    """
    datos_por_tipo = {}  # {nombre_clase: [distancias_medias]}

    for tipo_borracho in tipos_borracho:
        print(f"\n{'=' * 60}")
        print(f"Simulando: {tipo_borracho.__name__}")
        print(f"{'=' * 60}")

        distancias_media_por_caminata = []

        for pasos in distancia_caminata:
            distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
            distancia_media = round(sum(distancias) / len(distancias), 4)
            distancia_max = max(distancias)
            distancia_min = min(distancias)
            distancias_media_por_caminata.append(distancia_media)

            print(f"{tipo_borracho.__name__} caminata aleatoria de {pasos} pasos")
            print(
                f" Media = {distancia_media}\n Max = {distancia_max}\n Min = {distancia_min}"
            )

        datos_por_tipo[tipo_borracho.__name__] = distancias_media_por_caminata

    graficar(distancia_caminata, datos_por_tipo)


if __name__ == "__main__":
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_intentos = 100

    # Comparar ambos tipos de borracho en la misma gráfica
    main(
        distancias_de_caminata, numero_intentos, [BorrachoTradicional, BorrachoContinuo]
    )
# from bokeh.plotting import figure, show
# from borracho import BorrachoTradicional
# from campo import Campo
# from coordenada import Coordenada


# def main(distancia, inicio, borracho):
#     campo = Campo()
#     campo.add_borracho(borracho, inicio)  # poner un borracho en origen
#     ejecutar_caminata(campo, borracho, distancia)


# def ejecutar_caminata(campo, borracho, distancia):
#     x_arreglo = []
#     y_arreglo = []
#     x_arreglo.append(campo.obtener_coordenada(borracho).x)
#     y_arreglo.append(campo.obtener_coordenada(borracho).y)
#     for _ in range(distancia):
#         campo.mover_borracho(borracho)  # se actualiza las coordenadas del borracho
#         x_arreglo.append(campo.obtener_coordenada(borracho).x)
#         y_arreglo.append(campo.obtener_coordenada(borracho).y)

#     graficar(x_arreglo, y_arreglo)


# def graficar(x, y):
#     figura = figure()
#     figura.line(x, y)
#     show(figura)


# if __name__ == "__main__":
#     distancia = 1000000
#     inicio = Coordenada(0, 0)
#     borracho = BorrachoTradicional("Angel")
#     main(distancia, inicio, borracho)
