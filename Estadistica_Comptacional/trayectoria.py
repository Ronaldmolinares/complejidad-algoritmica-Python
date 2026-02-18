from bokeh.plotting import figure, show
from borracho import BorrachoTradicional
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


# VISUALIZACIÓN DE TRAYECTORIA COMPLETA
def visualizar_trayectoria(pasos, tipo_borracho):
    """Grafica el camino completo que toma el borracho paso a paso.

    Args:
        pasos: Número de pasos a simular
        tipo_borracho: Clase del borracho a usar
    """
    # Configuración inicial
    borracho = tipo_borracho(nombre="Juan")
    origen = Coordenada(0, 0)
    campo = Campo()
    campo.add_borracho(borracho, origen)

    # Listas para guardar TODAS las posiciones
    x_trayectoria = [0]  # Empieza en x=0
    y_trayectoria = [0]  # Empieza en y=0

    # Ejecutar la caminata y guardar cada posición
    for _ in range(pasos):
        campo.mover_borracho(borracho)  # Da un paso
        posicion_actual = campo.obtener_coordenada(borracho)
        x_trayectoria.append(posicion_actual.x)
        y_trayectoria.append(posicion_actual.y)

    # Calcular distancia final
    distancia_final = origen.distancia(posicion_actual)

    # Crear la gráfica
    grafica = figure(
        title=f"Trayectoria de {tipo_borracho.__name__} - {pasos} pasos",
        x_axis_label="Posición X",
        y_axis_label="Posición Y",
        width=800,
        height=800,
    )

    # Dibujar la trayectoria (línea azul)
    grafica.line(x_trayectoria, y_trayectoria, line_width=1, color="blue", alpha=0.6)

    # Marcar el INICIO (círculo verde)
    grafica.circle([0], [0], size=15, color="green", legend_label="Inicio (0,0)")

    # Marcar el FINAL (círculo rojo)
    grafica.circle(
        [x_trayectoria[-1]],
        [y_trayectoria[-1]],
        size=15,
        color="red",
        legend_label=f"Final ({x_trayectoria[-1]:.1f}, {y_trayectoria[-1]:.1f})",
    )

    grafica.legend.location = "top_left"

    print(f"\n{'=' * 60}")
    print(f"TRAYECTORIA DE {tipo_borracho.__name__}")
    print(f"{'=' * 60}")
    print(f"Pasos dados: {pasos}")
    print("Posición inicial: (0, 0)")
    print(f"Posición final: ({x_trayectoria[-1]:.2f}, {y_trayectoria[-1]:.2f})")
    print(f"Distancia total desde origen: {distancia_final:.2f}")
    print(f"{'=' * 60}\n")

    show(grafica)


if __name__ == "__main__":
    visualizar_trayectoria(pasos=1000, tipo_borracho=BorrachoTradicional)
