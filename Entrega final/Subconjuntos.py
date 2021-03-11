import Thompson as t
import Grafo as g
import NodoSubconjuntos as ns

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
        print(f"Compara estados {nodo.getEstados()} = {posibleNuevoEstado}")
        if (compararConjuntos(nodo.getEstados(), posibleNuevoEstado)):
            return True, id
    return False, None

def generarSubConjuntosIteracion(estadoPivote, NFA, estados, lenguaje):

    for letra in lenguaje:
        print(f"{estadoPivote}, {letra}")
        mover = t.mover(NFA, estados[estadoPivote].getEstados(), letra)
        print(f"mover = {mover}")

        if (len(mover) > 0):
            e_cerraduraTemp = t.e_cerradura(NFA, mover)
            print(f"e_cerraduraTemp = {e_cerraduraTemp}")
            estadoControl, idEstado = isNuevoEstado(estados, e_cerraduraTemp)
            print(f"EstadoControl = {estadoControl}, idEstado = {idEstado}")

            if (estadoControl):
                # Ya existe un estado igual, 
                # se crea relacion
                print("Crear relacion estado existente")
                print(f'{estadoPivote} -> {letra} ->{estadoPivote}')
                estados[estadoPivote].agregarRelacion(ns.RelacionSubconjuntos(estadoPivote, letra, estadoPivote))
            else:
                print("Crear relacion nuevo estado")
                nuevoEstadoLetraId = nextLetraId()
                print(f'{estadoPivote} -> {letra} ->{nuevoEstadoLetraId}')
                estados[nuevoEstadoLetraId] = ns.NodoSubconjuntos(False, e_cerraduraTemp)
                estados[estadoPivote].agregarRelacion(ns.RelacionSubconjuntos(estadoPivote, letra, nuevoEstadoLetraId))
        
        '''
        print(f"""

        lenguaje = {lenguaje}
        estados = {estados}
        *mover = {mover}
        colaLetrasId = {colaLetrasId}

        """)
        '''
    return estados


def generarSubConjuntos(NFA):
    #lenguaje = t.getLenguaje(NFA)
    lenguaje = ['a','b']
    estados = {}
    estadosRevisados = [] # los estados que ya se revisaron
    
    idNodoInicial, _ = t.getIdNodoInicio(NFA)

    # e-cerradura del estado inicial
    estados[nextLetraId()] = ns.NodoSubconjuntos(True, t.e_cerradura(NFAOR, [idNodoInicial]))


    while (len(colaLetrasId) > 0):
        ns.printNFDdebug(estados)
        estados = generarSubConjuntosIteracion(getLetraIdActual(), NFA, estados, lenguaje)

    
    # Se definen los estados finales
    idNodoFinal, _ = t.getIdNodoFin(NFA)
    estados = ns.setEstadosFinales(estados, idNodoFinal)
    

    g.visualizarNFD(estados)






if __name__ == '__main__':


    NFA1 = t.construirUnSimbolo("a")
    NFAKleen = t.construirKleen(NFA1)
    NFA2 = t.construirUnSimbolo("b")
    
    NFAOR = t.construirOr(NFAKleen, NFA2)

    generarSubConjuntos(NFAOR)

    #g.visualizarNFA(NFAOR)