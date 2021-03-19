from Nodo import Node
from itertools import product
from Preprocesador import preProcesarExpresion
import numpy as np
import Thompson as t
import Directo as d


class Arbol(object):
    """
    El objeto Arbol contiene metodos utiles
    para construir un arbol y recorrerlo.

    Variable
    ----------
    pila : list
        guarda la cola de objetos antes de
        llegar a un operador y construir los
        nodos del arbol
    operadores : list
        Operadores aceptados por el programa
    numeros : list
        Contiene todos los simbolos aceptados por
        el programa

    """

    def __init__(self):
        self.pila = []
        self.operadores = ['|', '*','.']
        self.numeros = list(map(str,range(0,10))) + ['ε','α','#'] + list(map(chr, range(ord('a'), ord('z')+1)))
        self.diccionario = {}


    def postOrder(self, Node):
        '''
        Recorre el arbol de forma postoperden
        y va construyendo los NFA usando el 
        algoritmo de Thompson

        Parametros
        ----------
        Node: Obj Node
            Nodo raiz del arbol

        '''

        # Si no existe raiz no seguimos
        if(Node == None):
            return

        # Ejecutamos postOrden en los nodos hijos
        self.postOrder(Node.getLeft())
        self.postOrder(Node.getRight())

        if(Node.getValue() in self.operadores):
            

            # Si el nodo actual es un Operadores
            if(Node.getValue() == '|'):
                NFA1 = self.pila[len(self.pila)-1]
                NFA2 = self.pila[len(self.pila)-2]

                self.pila.pop()
                self.pila.pop()

                self.pila.append(t.construirOr(NFA1, NFA2))

            if(Node.getValue() == '*'):
                NFA1 = self.pila[len(self.pila)-1]
                NFA2 = self.pila[len(self.pila)-2]

                self.pila.pop()
                self.pila.pop()

                self.pila.append(t.construirKleen(NFA2))


            if(Node.getValue() == '.'):
                NFA1 = self.pila[len(self.pila)-1]
                NFA2 = self.pila[len(self.pila)-2]
                

                self.pila.pop()
                self.pila.pop()

                self.pila.append(t.construirConcatenacion(NFA2, NFA1))


        else:
            # Si el nodo actual no es un operador
            self.pila.append(t.construirUnSimbolo(Node.getValue()))


    def interpretarEcuacion(self, entrada):      
        '''
        Recorre la expr y arma el arbol

        Parametros
        ----------
        entrada: str
            Expr ingresada
        
        Returns
        ----------
            NFA


        '''  
        root = Node(None)
        actual = root

        # Se arma el arbol
        for i in entrada:
            if(i == '('):
                # Se crea nodo izquiedo
                # Se mueve al nodo izquierdo
                actual.setLeft(None, actual)
                actual = actual.getLeft()

            if(i in self.operadores):
                # Se pone el valor al nodo: {i}
                # Se crea nodo derecho
                # Se mueve al nodo derecho
                actual.setValue(i)
                actual.setRight(None, actual)
                actual = actual.getRight()

            if(i in self.numeros):
                # Se pone el valor al nodo: {i}
                # Se mueve a la raiz del nodo
                actual.setValue(i)
                actual = actual.getRoot()

            if(i == ')'):
                # Se mueve a la raiz del nodo
                actual = actual.getRoot()

        self.postOrder(root)
        return self.pila[0]

    def armarArbol(self, entrada):
        '''
        Recorre la expr aumentada y 
        arma el arbol para el algoritmo directo

        Parametros
        ----------
        entrada: str
            Expr ingresada
        
        Returns
        ----------
            Nodo raiz


        '''
        root = Node(None)
        actual = root

        # Se arma el arbol
        for i in entrada:
            
            if(i == '('):
                # Se crea nodo izquiedo
                # Se mueve al nodo izquierdo
                actual.setLeft(None, actual)
                actual = actual.getLeft()

            if(i in self.operadores):
                # Se pone el valor al nodo: {i}
                # Se crea nodo derecho
                # Se mueve al nodo derecho
                actual.setValue(i)
                actual.setRight(None, actual)
                actual = actual.getRight()

            if(i in self.numeros):
                # Se pone el valor al nodo: {i}
                # Se mueve a la raiz del nodo
                actual.setValue(i)
                actual = actual.getRoot()

            if(i == ')'):
                # Se mueve a la raiz del nodo
                actual = actual.getRoot()

        return root