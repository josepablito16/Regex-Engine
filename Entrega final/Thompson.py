from NodoThompson import *
from Grafo import *


NFA = {}


def construirUnSimbolo(simbolo):
    NFA = {}
    NFA[1] = NodoThompson(True, False)
    NFA[2] = NodoThompson(False, True)

    NFA[1].agregarRelacion(RelacionThompson(1, simbolo, 2))
    
    visualizarNFA(NFA)

    



if __name__ == '__main__':
    construirUnSimbolo("b")