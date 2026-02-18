from dataclasses import dataclass


@dataclass
class Coordenada:
    """Representa una posición (x, y) en un plano"""

    x: int
    y: int

    def mover(self, delta_x, delta_y):
        """Crea una nueva coordenada sumando deltas
        Retorna: Un objeto Coordenada NUEVO con la posición actualizada
        """
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def distancia(self, otra_coordenada):
        """calcula distancia euclidiana entre dos puntos"""
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2) ** 0.5
