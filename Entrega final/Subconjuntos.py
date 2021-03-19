import Thompson as t
import Grafo as g
import NodoSubconjuntos as ns

"""
Este script contiene funciones utiles para 
la generacion de subconjuntos

Variable
----------
letrasId : list
    guarda una lista con todas las letras de la A - Z,
    los cuales seran los identificadores de los nodos
colaLetrasId : list
    cola de los estados por ser procesados
"""

letrasId = list(map(chr, range(ord('A'), ord('Z')+1)))
colaLetrasId =[]

def nextLetraId():
    nextLetra = letrasId.pop(0)
    colaLetrasId.append(nextLetra)
    return nextLetra

def getLetraIdActual():
    return colaLetrasId.pop(0)

def getLetraEnCurso():
    return colaLetrasId[0]

# Compara si dos listas son equivalentes
def compararConjuntos(conjunto1, conjunto2):
    return set(conjunto1).issubset(set(conjunto2)) and len(conjunto1) == len(conjunto2)

# Revisa si el nuevo estado es 
# equivalente a uno existente
def isNuevoEstado(estados, posibleNuevoEstado):
    for id, nodo in estados.items():
        if (compararConjuntos(nodo.getEstados(), posibleNuevoEstado)):
            return True, id
    return False, None

def generarSubConjuntosIteracion(estadoPivote, NFA, estados, lenguaje):

    for letra in lenguaje:
        # mover dado un Estado y una letra
        mover = t.mover(NFA, estados[estadoPivote].getEstados(), letra)

        if (len(mover) > 0):
            # Calcular e_cerradura
            e_cerraduraTemp, _ = t.e_cerradura(NFA, mover)
            e_cerraduraTemp = list(set(e_cerraduraTemp))

            # Se revisa si el estado generado es nuevo o existente
            estadoControl, idEstado = isNuevoEstado(estados, e_cerraduraTemp)

            if (estadoControl):
                # Ya existe un estado igual, 
                # se crea relacion
                estados[estadoPivote].agregarRelacion(ns.RelacionSubconjuntos(estadoPivote, letra, idEstado))
            else:
                nuevoEstadoLetraId = nextLetraId()
                estados[nuevoEstadoLetraId] = ns.NodoSubconjuntos(False, e_cerraduraTemp)
                estados[estadoPivote].agregarRelacion(ns.RelacionSubconjuntos(estadoPivote, letra, nuevoEstadoLetraId))
        
    return estados


def generarSubConjuntos(NFA):
    lenguaje = t.getLenguaje(NFA)
    estados = {}
    estadosRevisados = [] # los estados que ya se revisaron
    
    idNodoInicial, _ = t.getIdNodoInicio(NFA)

    # e-cerradura del estado inicial
    e_cerraduraTemp, _ = t.e_cerradura(NFA, [idNodoInicial])
    
    estados[nextLetraId()] = ns.NodoSubconjuntos(True,list(set(e_cerraduraTemp)))

    # Se itera hasta quedarse sin estados por procesar
    while (len(colaLetrasId) > 0):
        
        estados = generarSubConjuntosIteracion(getLetraIdActual(), NFA, estados, lenguaje)

    
    # Se definen los estados finales
    idNodoFinal, _ = t.getIdNodoFin(NFA)
    estados = ns.setEstadosFinales(estados, idNodoFinal)
    
    return estados



def simularNFD(NFD, cadena):
    s = ns.getEstadosIniciales(NFD)[0]

    for i in cadena:
        if (s == []):
            break
        s = ns.mover(NFD[s],i)
    

    # Si la interseccion de S y los estados finales no es vacia
    # Entonces se acepta la cadena
    if (list(set.intersection(set(s),set(ns.getEstadosFinales(NFD)))) != []):
        return "SI"
    else:
        return "NO"


if __name__ == '__main__':


    NFA1 = t.construirUnSimbolo("a")
    NFAKleen = t.construirKleen(NFA1)
    NFA2 = t.construirUnSimbolo("b")
    
    NFAOR = t.construirOr(NFAKleen, NFA2)

    generarSubConjuntos(NFAOR)

    #g.visualizarNFA(NFAOR)