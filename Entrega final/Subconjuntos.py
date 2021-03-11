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
        mover = t.mover(NFA, estados[estadoPivote].getEstados(), letra)

        if (len(mover) > 0):
            e_cerraduraTemp = t.e_cerradura(NFA, mover)
            print(e_cerraduraTemp)
            estadoControl, idEstado = isNuevoEstado(estados, e_cerraduraTemp)

            if (estadoControl):
                # Ya existe un estado igual, 
                # se crea relacion
                print("Crear relacion estado existente")
            else:
                estados[nextLetraId()] = ns.NodoSubconjuntos(False, e_cerraduraTemp)
                print("Crear relacion nuevo estado")
        
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
    lenguaje = t.getLenguaje(NFA)
    estados = {}
    estadosRevisados = [] # los estados que ya se revisaron
    
    idNodoInicial, _ = t.getIdNodoInicio(NFA)

    # e-cerradura del estado inicial
    estados[nextLetraId()] = ns.NodoSubconjuntos(True, t.e_cerradura(NFAOR, [idNodoInicial]))

    while (len(colaLetrasId) > 0):
        print(colaLetrasId)
        estados = generarSubConjuntosIteracion(getLetraIdActual(), NFA, estados, lenguaje)
    
    print(estados)






if __name__ == '__main__':
    '''
    A = [1,2,3]
    B = [2,3,1]
    C = [1,2,5]

    print(f"A y B = {compararConjuntos(A,B)}")
    print(f"A y C = {compararConjuntos(A,C)}")

    print(alphabets.pop(0))
    print(alphabets)
    '''

    NFA1 = t.construirUnSimbolo("a")
    NFAKleen = t.construirKleen(NFA1)
    NFA2 = t.construirUnSimbolo("b")
    
    NFAOR = t.construirOr(NFAKleen, NFA2)
    print()
    print(NFAOR)
    print()
    generarSubConjuntos(NFAOR)

    #g.visualizarNFA(NFAOR)