# Definição utilizando enumeração
#
# Autor: Fabrício Galende Marques de Carvalho

from enum import Enum, auto

class Mes(Enum):
    JANEIRO = 1
    FEVEREIRO = auto()
    MARCO = auto()
    ABRIL = auto()
    MAIO = auto()
    JUNHO = auto()
    JULHO = auto()
    AGOSTO = auto()
    SETEMBRO = auto()
    OUTUBRO = auto()
    NOVEMBRO = auto()
    DEZEMBRO = auto()