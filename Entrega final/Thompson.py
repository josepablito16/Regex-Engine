import NodoThompson as nt
import Grafo as g

def construirUnSimbolo(simbolo):
    NFA = {}
    NFA[1] = nt.NodoThompson(True, False)
    NFA[2] = nt.NodoThompson(False, True)

    NFA[1].agregarRelacion(nt.RelacionThompson(1, simbolo, 2))
    return NFA
    

def construirOr(NFA1, NFA2):
    # Se crea el NFA y su estado inicial
    NFA = {}
    NFA[1] = nt.NodoThompson(True, False)

    # Se actualizan los ids de los NFAs
    idContador = 1
    NFA1, idContador = nt.actualizarIdsNodos(NFA1, idContador)

    NFA2, idContador = nt.actualizarIdsNodos(NFA2, idContador)


    # Se obtiene el estado inicial y final de
    # NFA1 y tambien se quitan los estados locales
    idInicial1, NFA1 = nt.getIdInicial(NFA1)
    idFinal1, NFA1 = nt.getIdFinal(NFA1)
 
    # Se obtiene el estado inicial y final de
    # NFA2 y tambien se quitan los estados locales
    idInicial2, NFA2 = nt.getIdInicial(NFA2)
    idFinal2, NFA2 = nt.getIdFinal(NFA2)
    
    # Join de NFAs
    NFA.update(NFA2)
    NFA.update(NFA1)
    #print(f"NFA = {NFA}")

    # Se crean las relaciones del nodo inicial
    #print(f"Id Iniciales {[idInicial1, idInicial2]}")
    NFA[1].agregarRelacion(nt.RelacionThompson(1, "ε", idInicial1))
    NFA[1].agregarRelacion(nt.RelacionThompson(1, "ε", idInicial2))

    # Se crea el nodo final
    idContador += 1
    NFA[idContador] = nt.NodoThompson(False, True)

    # Se crean las relaciones para el nodo final
    NFA[idFinal1].agregarRelacion(nt.RelacionThompson(idFinal1, "ε", idContador))
    NFA[idFinal2].agregarRelacion(nt.RelacionThompson(idFinal2, "ε", idContador))

    return NFA

    
def construirKleen(NFA1):
    # Se crea el NFA y su estado inicial
    NFA = {}
    NFA[1] = nt.NodoThompson(True, False)

    # Se actualizan los ids de los NFAs
    idContador = 1
    NFA1, idContador = nt.actualizarIdsNodos(NFA1, idContador)

    # Se obtiene el estado inicial y final de
    # NFA1 y tambien se quitan los estados locales
    idInicial1, NFA1 = nt.getIdInicial(NFA1)
    idFinal1, NFA1 = nt.getIdFinal(NFA1)

    # Join de NFAs
    NFA.update(NFA1)

    # Se crea el nodo final
    idContador += 1
    NFA[idContador] = nt.NodoThompson(False, True)

    # Se crean las relaciones del nodo inicial
    NFA[1].agregarRelacion(nt.RelacionThompson(1, "ε", idInicial1))
    NFA[1].agregarRelacion(nt.RelacionThompson(1, "ε", idContador))

    # Se agregan relaciones del NFA1
    NFA[idFinal1].agregarRelacion(nt.RelacionThompson(idFinal1, "ε", idInicial1))
    NFA[idFinal1].agregarRelacion(nt.RelacionThompson(idFinal1, "ε", idContador))

    return NFA


def construirConcatenacion(NFA1, NFA2):
    # Se crea el NFA
    NFA = {}

    # Se actualizan los ids del NFA2
    idContador = max(NFA1.keys())
    NFA2, idContador = nt.actualizarIdsNodos(NFA2, idContador)

    # Se obtiene el estado final de NFA1
    idFinal1, NFA1 = nt.getIdFinal(NFA1)

    # Se obtiene el estado inicial de NFA2
    idInicial2, NFA2 = nt.getIdInicial(NFA2)

    # Join de NFAs
    NFA.update(NFA1)
    NFA.update(NFA2)

    #print(NFA)
    NFA = nt.mergeEstados(NFA, idFinal1, idInicial2)
    #print(NFA)

    # Merge estados
    return NFA

def getLenguaje(NFA):
    lenguaje = []
    for nodo in NFA.values():
        relaciones = nodo.getRelaciones()
        if (len(relaciones) > 1):
            for relacion in relaciones:
                lenguaje.append(relacion[2])
        elif(len(relaciones) != 0):
            lenguaje.append(relaciones[0][2])
    
    lenguajeFinal = []
    for i in set(lenguaje):
        if (i != 'ε'):
            lenguajeFinal.append(i)
    
    return lenguajeFinal


def e_cerradura(NFA, estado, visitados = []):
    elementos = []
    elementos += estado
    
    for elemento in estado:
        for nodo in NFA.values():
            relaciones = nodo.getRelaciones()
            if (len(relaciones) > 1):
                for relacion in relaciones:
                    if (elemento == relacion[0] and relacion[2] =='ε'):
                        #print(relacion[1])
                        if (relacion[1] in visitados):
                            continue
                        visitados.append(relacion[1])
                        elementos += e_cerradura(NFA, [relacion[1]], visitados)
            elif(len(relaciones) != 0):
                if (elemento == relaciones[0][0] and relaciones[0][2] =='ε'):
                    #print(relaciones[0][1])
                    if (relaciones[0][1] in visitados):
                        continue
                    visitados.append(relaciones[0][1])
                    elementos += e_cerradura(NFA, [relaciones[0][1]], visitados)

    return elementos

def getIdNodoInicio(NFA):
    return nt.getIdInicial(NFA)

def getIdNodoFin(NFA):
    return nt.getIdFinal(NFA)

def mover(NFA, estado, simbolo):
    elementos = []
    
    for elemento in estado:
        for nodo in NFA.values():
            relaciones = nodo.getRelaciones()
            if (len(relaciones) > 1):
                for relacion in relaciones:
                    if (elemento == relacion[0] and relacion[2] == simbolo):
                        #print(relacion[1])
                        elementos.append(relacion[1])
            elif(len(relaciones) != 0):
                if (elemento == relaciones[0][0] and relaciones[0][2] == simbolo):
                    #print(relaciones[0][1])
                    elementos.append(relaciones[0][1])
    return elementos





if __name__ == '__main__':
    NFA1 = construirUnSimbolo("a")
    NFA2 = construirUnSimbolo("b")
    
    NFAOR = construirOr(NFA1, NFA2)

    NFAKleen = construirKleen(NFAOR)

    NFA3 = construirUnSimbolo("b")

    concatenacion1 = construirConcatenacion(NFAKleen, NFA3)

    NFA4 = construirUnSimbolo("b")

    g.visualizarNFA(construirConcatenacion(concatenacion1, NFA4))