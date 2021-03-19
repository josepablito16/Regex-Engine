from Nodo import Node
import NodoDirecto as nd
import Grafo as g

"""
Script con funciones utiles para el algoritmo
directo

Variable
----------
contador : int
    se usa como id para las hojas

operadores : list
    Operadores aceptados por el programa
numeros : list
    Contiene todos los simbolos aceptados por
    el programa

nodosHoja : dict
    Guarda los nodos de las hojas del arbol

followPos : dict
    Guarda followPos para cada uno de los elementos

letrasId : list
    Tiene todas las letras mayusculas de A - Z
    Se usa para los identificadores del grafo

colaLetrasId : list
    Contiene los estados en cola para el algoritmo

"""

numeros = list(map(str,range(0,10))) + ['ε','α','#'] + list(map(chr, range(ord('a'), ord('z')+1)))
operadores = ['|', '*','.']
contador = 1
nodosHoja ={}
followPos = {}

letrasId = list(map(chr, range(ord('A'), ord('Z')+1)))
colaLetrasId =[]


def compararEstados(idsValidos, estadosCreados):
    '''
    Compara dos listas, retorna si son iguales True
    sino False
    '''
    for estado in estadosCreados:
        if(
            list(set(idsValidos) - set(estado))
            ==
            list(set(estado) - set(idsValidos))
            ==
            []
        ):
            return True
    return False

def nextLetraId():
    '''
    Retorna la siguiente letra y la 
    agrega a la cola para evaluarla luego
    '''
    nextLetra = letrasId.pop(0)
    colaLetrasId.append(nextLetra)
    return nextLetra

def union(lista):
    '''
    Quita elementos repetidos de una lista
    '''
    return list(set(lista))

def postOrder(Node):
    '''
    Recorre el arbol postOrden para calcular
    nullable, firstpos y lastPos
    '''
    if(Node == None):
        return

    postOrder(Node.getLeft())
    postOrder(Node.getRight())

    if(Node.getValue() in operadores):
        # Operadores
        if(Node.getValue() == '|'):
            calcularNullableOr(Node)
            calcularFirstLastPosOr(Node)
        
        if(Node.getValue() == '*'):
            calcularNullableStar(Node)
            calcularFirstLastPosStar(Node)
            calcularFollowPosStar(Node)
        
        if(Node.getValue() == '.'):
            calcularNullableConcat(Node)
            calcularFirstLastPosConcat(Node)
            calcularFollowPosConcat(Node)
        
        
        Node.info()

    else:
        if (Node.getValue() in numeros):
            calcularFirstLastPosHoja(Node)
            calcularNullableHoja(Node)
            Node.info()

# Calculo de funciones concat
def calcularNullableConcat(nodo):
    nodo.setNullable(nodo.getLeft().isNullable() and nodo.getRight().isNullable())

def calcularFirstLastPosConcat(nodo):
    if (nodo.getLeft().isNullable()):
        nodo.addFirstPos(
            union(
                nodo.getLeft().getFirstPos()
                +
                nodo.getRight().getFirstPos()
            )
        )
    else:
        nodo.addFirstPos(
            nodo.getLeft().getFirstPos()
            )
    
    if (nodo.getRight().isNullable()):
        nodo.addLastPos(
            union(
                nodo.getLeft().getLastPos()
                +
                nodo.getRight().getLastPos()
            )
        )
    else:
        nodo.addLastPos(nodo.getRight().getLastPos())

def calcularFollowPosConcat(nodo):
    for i in nodo.getLeft().getLastPos():
        followPos[i] += nodo.getRight().getFirstPos()

# Calculo de funciones *
def calcularFollowPosStar(nodo):
    for i in nodo.getLastPos():
        followPos[i] += nodo.getFirstPos()

def calcularNullableStar(nodo):
    nodo.setNullable(True)

def calcularFirstLastPosStar(nodo):
    nodo.addFirstPos(
        nodo.getLeft().getFirstPos()
    )
    nodo.addLastPos(
        nodo.getLeft().getLastPos()
    )

# Calculo de funciones OR
def calcularNullableOr(nodo):
    nodo.setNullable(nodo.getLeft().isNullable() or nodo.getRight().isNullable())

def calcularFirstLastPosOr(nodo):
    nodo.addFirstPos(
        union(
            nodo.getLeft().getFirstPos()
            +
            nodo.getRight().getFirstPos()
        )
    )
    nodo.addLastPos(
        union(
            nodo.getLeft().getLastPos()
            +
            nodo.getRight().getLastPos()
        )
    )

# Calculo de funciones hojas
def calcularNullableHoja(nodo):
    if (nodo.getValue() in numeros):
        if (nodo.getValue() == 'ε'):
            nodo.setNullable(True)
        else:
            nodo.setNullable(False)

def calcularFirstLastPosHoja(nodo):
    global contador
    if (nodo.getValue() in numeros):
        try:
            nodosHoja[nodo.getValue()].append(contador)
            
        except:
            nodosHoja[nodo.getValue()] = [contador]
        followPos[contador] = []
        if (nodo.getValue() == 'ε'):
            pass
        else:
            nodo.addFirstPos([contador])
            nodo.addLastPos([contador])
        contador += 1
 

def construirDFA(estadoInicial):
    '''
    Funcion para construir DFA con el algoritmo
    Directo
    '''

    pilaDeEstados=[estadoInicial]
    estadosCreados = [estadoInicial]
    DFA = {}
    DFA[nextLetraId()] = nd.NodoDirecto(estadoInicial, True)


    while len(pilaDeEstados) > 0:
        estadoActual = pilaDeEstados.pop()
        letraActual = colaLetrasId.pop()
        
        for letra, ids in nodosHoja.items():
            if (letra =="#"):
                continue
            
            idsValidos = []
            
            for id in ids:
                if (id in estadoActual):
                    idsValidos += followPos[id]

            if not (compararEstados(idsValidos, estadosCreados)):
                if (idsValidos == []):
                    continue
                
                pilaDeEstados.append(list(set(idsValidos)))
                estadosCreados.append(list(set(idsValidos)))

                # agregar relacion a DFA
                letraTemp = nextLetraId()
                colaLetrasId.append(letraTemp)
                DFA[letraTemp] = nd.NodoDirecto(list(set(idsValidos)))

                # crear relacion con nuevo estado
                DFA[nd.getLetraDeEstados(DFA, list(set(estadoActual)))].agregarRelacion(nd.RelacionDirecto(nd.getLetraDeEstados(DFA, list(set(estadoActual))), letra, letraTemp))
        
            else:
                # crear relacion con un estado existente
                DFA[nd.getLetraDeEstados(DFA, list(set(estadoActual)))].agregarRelacion(nd.RelacionDirecto(nd.getLetraDeEstados(DFA, list(set(estadoActual))), letra, nd.getLetraDeEstados(DFA, list(set(idsValidos)))))

    
    # Revisar estados finales
    DFA = nd.setEstadosFinales(DFA, contador - 1)
    return DFA



def construirFuncionesBasicas(nodo):
    '''
    Recorre el arbol y calcula las funciones basicas
    '''

    postOrder(nodo)

    DFA = construirDFA(nodo.getFirstPos())
    return DFA
    

    
def simularDirecto(DFA, cadena):
    '''
    Simula DFA dada una cadena
    '''

    s = nd.getEstadosIniciales(DFA)[0]
    
    for i in cadena:
        if (s == []):
            break
        s = nd.mover(DFA[s],i)
    

    # Si la interseccion de S y los estados finales no es vacia
    # Entonces se acepta la cadena
    if (list(set.intersection(set(s),set(nd.getEstadosFinales(DFA)))) != []):
        return "SI"
    else:
        return "NO"