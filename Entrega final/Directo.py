from Nodo import Node

numeros = ['a', 'b','ε','#']
operadores = ['|', '*','.']
contador = 1


def postOrder(Node):
    if(Node == None):
        return

    postOrder(Node.getLeft())
    postOrder(Node.getRight())

    if(Node.getValue() in operadores):
        # Operadores
        if(Node.getValue() == '|'):
            pass
            #print(f"{num1} + {num2}")

            #pila.append(t.construirOr(NFA1, NFA2)

    else:
        if (Node.getValue() in numeros):
            getInfo(Node)

def getInfo(nodo):
    global contador
    nodo.addFirstPos(contador)
    nodo.addLastPos(contador)
    contador += 1
    nodo.info()

def construirFuncionesBasicas(nodo):
    postOrder(nodo)
    