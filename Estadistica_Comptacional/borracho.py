# Los caminos aleatorios se utilizan en fenomenos fisicos, comportamientos a lo largo del tiempo

# Caminos aleatorios

import random
from dataclasses import dataclass


@dataclass
class Borracho:
    nombre: str


class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
