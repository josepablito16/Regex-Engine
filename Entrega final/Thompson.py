from NodoThompson import *
from Grafo import *

def construirUnSimbolo(simbolo):
    NFA = {}
    NFA[1] = NodoThompson(True, False)
    NFA[2] = NodoThompson(False, True)

    NFA[1].agregarRelacion(RelacionThompson(1, simbolo, 2))
    return NFA
    

def construirOr(NFA1, NFA2):
    # Se crea el NFA y su estado inicial
    NFA = {}
    NFA[1] = NodoThompson(True, False)

    # Se actualizan los ids de los NFAs
    idContador = 1
    NFA1, idContador = actualizarIdsNodos(NFA1, idContador)

    NFA2, idContador = actualizarIdsNodos(NFA2, idContador)


    # Se obtiene el estado inicial y final de
    # NFA1 y tambien se quitan los estados locales
    idInicial1, NFA1 = getIdInicial(NFA1)
    idFinal1, NFA1 = getIdFinal(NFA1)
 
    # Se obtiene el estado inicial y final de
    # NFA2 y tambien se quitan los estados locales
    idInicial2, NFA2 = getIdInicial(NFA2)
    idFinal2, NFA2 = getIdFinal(NFA2)
    
    # Join de NFAs
    NFA.update(NFA2)
    NFA.update(NFA1)
    print(f"NFA = {NFA}")

    # Se crean las relaciones del nodo inicial
    print(f"Id Iniciales {[idInicial1, idInicial2]}")
    NFA[1].agregarRelacion(RelacionThompson(1, "ε", idInicial1))
    NFA[1].agregarRelacion(RelacionThompson(1, "ε", idInicial2))

    # Se crea el nodo final
    idContador += 1
    NFA[idContador] = NodoThompson(False, True)

    # Se crean las relaciones para el nodo final
    NFA[idFinal1].agregarRelacion(RelacionThompson(idFinal1, "ε", idContador))
    NFA[idFinal2].agregarRelacion(RelacionThompson(idFinal2, "ε", idContador))

    return NFA

    
def construirKleen(NFA1):
    # Se crea el NFA y su estado inicial
    NFA = {}
    NFA[1] = NodoThompson(True, False)

    # Se actualizan los ids de los NFAs
    idContador = 1
    NFA1, idContador = actualizarIdsNodos(NFA1, idContador)

    # Se obtiene el estado inicial y final de
    # NFA1 y tambien se quitan los estados locales
    idInicial1, NFA1 = getIdInicial(NFA1)
    idFinal1, NFA1 = getIdFinal(NFA1)

    # Join de NFAs
    NFA.update(NFA1)

    # Se crea el nodo final
    idContador += 1
    NFA[idContador] = NodoThompson(False, True)

    # Se crean las relaciones del nodo inicial
    NFA[1].agregarRelacion(RelacionThompson(1, "ε", idInicial1))
    NFA[1].agregarRelacion(RelacionThompson(1, "ε", idContador))

    # Se agregan relaciones del NFA1
    NFA[idFinal1].agregarRelacion(RelacionThompson(idFinal1, "ε", idInicial1))
    NFA[idFinal1].agregarRelacion(RelacionThompson(idFinal1, "ε", idContador))

    return NFA



    



if __name__ == '__main__':
    NFA1 = construirUnSimbolo("a")
    NFA2 = construirUnSimbolo("b")
    
    NFAOR = construirOr(NFA1, NFA2)

    NFAKleen = construirKleen(NFAOR)
    visualizarNFA(NFAKleen)