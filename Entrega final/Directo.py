from Nodo import Node

numeros = ['a', 'b','ε','#']
operadores = ['|', '*','.']
contador = 1

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
        
        if(Node.getValue() == '.'):
            calcularNullableConcat(Node)
            calcularFirstLastPosConcat(Node)
        
        
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


# Calculo de funciones *
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
        if (nodo.getValue() == 'ε'):
            pass
        else:
            nodo.addFirstPos([contador])
            nodo.addLastPos([contador])
        contador += 1
 
    
    

def construirFuncionesBasicas(nodo):
    postOrder(nodo)
    