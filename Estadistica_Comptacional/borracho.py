# Los caminos aleatorios se utilizan en fenomenos fisicos, comportamientos a lo largo del tiempo

# Caminos aleatorios

import random
from dataclasses import dataclass


# Sirve para considerar a un @dataclass inmutable
# (ya que se tiene un diccionario donde la key viene siendo el objeto de esta clase)
@dataclass(frozen=True)
class Borracho:
    """Define el comportamiento aleatorio"""

    nombre: str


class BorrachoTradicional(Borracho):
    """Borracho con movimiento DISCRETO: pasos fijos de tamaño 1 en 4 direcciones"""

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        """Elige aleatoriamente una dirección cardinal (paso fijo de tamaño 1)"""
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])


class BorrachoContinuo(Borracho):
    """Borracho con movimiento CONTINUO: pasos variables entre 0-1 en todas direcciones"""

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        """Paso aleatorio con magnitud variable (más realista)"""
        return random.choice(
            [
                (random.random(), random.random()),  # Cuadrante 1
                (random.random() * -1, random.random()),  # Cuadrante 2
                (random.random() * -1, random.random() * -1),  # Cuadrante 3
                (random.random(), random.random() * -1),  # Cuadrante 4
            ]
        )
