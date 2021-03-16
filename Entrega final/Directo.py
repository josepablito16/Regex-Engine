from Nodo import Node
import NodoDirecto as nd
import Grafo as g

numeros = ['a', 'b','ε','#']
operadores = ['|', '*','.']
contador = 1
nodosHoja ={}
followPos = {}

letrasId = list(map(chr, range(ord('A'), ord('Z')+1)))
colaLetrasId =[]

def nextLetraId():
    nextLetra = letrasId.pop(0)
    colaLetrasId.append(nextLetra)
    return nextLetra

def union(lista):
    return list(set(lista))

def postOrder(Node):
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
    pilaDeEstados=[estadoInicial]
    estadosCreados = [estadoInicial]
    DFA = {}
    DFA[nextLetraId()] = nd.NodoDirecto(estadoInicial, True)


    while len(pilaDeEstados) > 0:
        estadoActual = pilaDeEstados.pop()
        letraActual = colaLetrasId.pop(0)
        for letra, ids in nodosHoja.items():
            if (letra =="#"):
                continue
            
            idsValidos = []
            
            for id in ids:
                if (id in estadoActual):
                    idsValidos += followPos[id]

            if not (idsValidos in estadosCreados):
                pilaDeEstados.append(idsValidos)
                estadosCreados.append(idsValidos)

                # agregar relacion a DFA
                letraTemp = nextLetraId()
                DFA[letraTemp] = nd.NodoDirecto(idsValidos)

                # crear relacion con nuevo estado
                DFA[letraActual].agregarRelacion(nd.RelacionDirecto(letraActual, letra, letraTemp))
                print(f"{letraActual} -> {letra} -> {letraTemp}")
            else:
                # crear relacion con un estado existente
                print(f"{letraActual} -> {letra} -> {nd.getLetraDeEstados(DFA, idsValidos)}")
                DFA[letraActual].agregarRelacion(nd.RelacionDirecto(letraActual, letra, nd.getLetraDeEstados(DFA, idsValidos)))

    
    # Revisar estados finales
    DFA = nd.setEstadosFinales(DFA, contador - 1)
    return DFA



def construirFuncionesBasicas(nodo):
    postOrder(nodo)

    print(f"""
    nodosHoja = {nodosHoja}
    followPos = {followPos}
    """)

    DFA = construirDFA(nodo.getFirstPos())
    g.visualizarDirecto(DFA)

    
    