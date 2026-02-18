from dataclasses import dataclass, field


@dataclass
class Campo:
    """Maneja el espacio donde se mueve el borracho"""

    coordenadas_de_borrachos: dict = field(default_factory=dict)

    def add_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        """Obtiene una dirección aleatoria y actualiza la posición"""
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]
