import Thompson as t
import Grafo as g

letrasId = list(map(chr, range(ord('A'), ord('Z')+1)))

def compararConjuntos(conjunto1, conjunto2):
    return set(conjunto1).issubset(set(conjunto2)) and len(conjunto1) == len(conjunto2)

def generarSubConjuntos(NFA):
    lenguaje = t.getLenguaje(NFA)
    estados = {}
    estadosRevisados = [] # los estados que ya se revisaron
    
    idNodoInicial, _ = t.getIdNodoInicio(NFA)


    estados[letrasId.pop(0)] = t.e_cerradura(NFAOR, [idNodoInicial])
    
    mover = list(set(t.mover(NFA, estados['A'], 'a')) - set(estados['A']))
    print(f"""
    lenguaje = {lenguaje}
    idNodoInicial = {idNodoInicial}
    estados = {estados}
    *mover = {mover}
    """)






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