from Nodo import Node
from itertools import product
from Preprocesador import preProcesarExpresion
import numpy as np
import Thompson as t
import Directo as d


class Arbol(object):
    """docstring for Arbol"""

    def __init__(self):
        self.pila = []
        self.operadores = ['|', '*','.']
        self.numeros = ['a', 'b','ε','α','#']
        self.diccionario = {}


    def postOrder(self, Node):
        if(Node == None):
            return

        self.postOrder(Node.getLeft())
        self.postOrder(Node.getRight())

        if(Node.getValue() in self.operadores):
            print(f" Operador {Node.getValue()}")

            # Operadores
            if(Node.getValue() == '|'):
                NFA1 = self.pila[len(self.pila)-1]
                NFA2 = self.pila[len(self.pila)-2]

                self.pila.pop()
                self.pila.pop()
                #print(f"{num1} + {num2}")

                self.pila.append(t.construirOr(NFA1, NFA2))

            if(Node.getValue() == '*'):
                NFA1 = self.pila[len(self.pila)-1]
                NFA2 = self.pila[len(self.pila)-2]

                

                self.pila.pop()
                self.pila.pop()
                #print(f"{num1} - {num2}")

                self.pila.append(t.construirKleen(NFA2))


            if(Node.getValue() == '.'):
                NFA1 = self.pila[len(self.pila)-1]
                NFA2 = self.pila[len(self.pila)-2]
                
                print()
                print("PRESTAR ATENCION")

                print(NFA1)
                print(NFA2)
                print()

                self.pila.pop()
                self.pila.pop()
                #print(f"{num1} / {num2}")

                self.pila.append(t.construirConcatenacion(NFA2, NFA1))

            if(Node.getValue() == '^'):
                num1 = self.pila[len(self.pila)-1]
                num2 = self.pila[len(self.pila)-2]

                self.pila.pop()
                self.pila.pop()
                #print(f"{num1} / {num2}")

                self.pila.append(self.exp(float(num1), float(num2)))

        else:
            print(f"No Operador {Node.getValue()}")
            self.pila.append(t.construirUnSimbolo(Node.getValue()))
        # print("ECUACION")
        # print(self.ecuacion)

    def postOrderDirecto(self, Node):
        if(Node == None):
            return

        self.postOrderDirecto(Node.getLeft())
        self.postOrderDirecto(Node.getRight())

        if(Node.getValue() in self.operadores):
            print(Node.getValue())
            #print(f" Operador {Node.getValue()}")

            # Operadores
            if(Node.getValue() == '|'):
                num1 = self.pila[len(self.pila)-1]
                num2 = self.pila[len(self.pila)-2]

                self.pila.pop()
                self.pila.pop()
                #print(f"{num1} | {num2}")
                self.pila.append(f"({num1} | {num2})")

            if(Node.getValue() == '*'):
                num1 = self.pila[len(self.pila)-1]
                num2 = self.pila[len(self.pila)-2]

                self.pila.pop()
                self.pila.pop()
                #print(f"{num2}*")
                self.pila.append(f"{num2}*")


            if(Node.getValue() == '.'):
                num1 = self.pila[len(self.pila)-1]
                num2 = self.pila[len(self.pila)-2]
                
                self.pila.pop()
                self.pila.pop()
                #print(f"{num1} . {num2}")
                self.pila.append(f"{num1} . {num2}")

        else:
            print(Node.getValue())
            #print(f"No Operador {Node.getValue()}")
            self.pila.append(Node.getValue())
        # print("ECUACION")
        # print(self.ecuacion)

    def interpretarEcuacion(self, entrada):
        entrada = preProcesarExpresion(entrada)
        entrada = "(((a.((b.a).((b.a)*α)))|((a.(b*α)).a))|(a|b))"
        print(entrada)
        root = Node(None)
        actual = root

        print("Se arma el arbol")
        for i in entrada:
            print(f"\nElemento : {i}")
            if(i == '('):
                print("Se crea nodo izquiedo")
                print("Se mueve al nodo izquierdo")
                actual.setLeft(None, actual)
                actual = actual.getLeft()

            if(i in self.operadores):
                print(f"Se pone el valor al nodo: {i}")
                print("Se crea nodo derecho")
                print("Se mueve al nodo derecho")
                actual.setValue(i)
                actual.setRight(None, actual)
                actual = actual.getRight()

            if(i in self.numeros):
                print(f"Se pone el valor al nodo: {i}")
                print("Se mueve a la raiz del nodo")
                actual.setValue(i)
                actual = actual.getRoot()

            if(i == ')'):
                print("Se mueve a la raiz del nodo")
                actual = actual.getRoot()
        '''
		print("Esta es")
		print(root.getValue())
		print(root.getLeft().getValue())
		print(root.getLeft().getLeft().getValue())
		'''
        # print("postOrder")
        self.postOrder(root)
        return self.pila[0]

    def armarArbol(self, entrada):
        #entrada = preProcesarExpresion(entrada)
        #entrada = "((ε|((a*α).b)).#)"
        #entrada = "((((((a|b)*α).a).b).b).#)"
        print(entrada)
        root = Node(None)
        actual = root

        print("Se arma el arbol")
        for i in entrada:
            print(f"\nElemento : {i}")
            if(i == '('):
                print("Se crea nodo izquiedo")
                print("Se mueve al nodo izquierdo")
                actual.setLeft(None, actual)
                actual = actual.getLeft()

            if(i in self.operadores):
                print(f"Se pone el valor al nodo: {i}")
                print("Se crea nodo derecho")
                print("Se mueve al nodo derecho")
                actual.setValue(i)
                actual.setRight(None, actual)
                actual = actual.getRight()

            if(i in self.numeros):
                print(f"Se pone el valor al nodo: {i}")
                print("Se mueve a la raiz del nodo")
                actual.setValue(i)
                actual = actual.getRoot()

            if(i == ')'):
                print("Se mueve a la raiz del nodo")
                actual = actual.getRoot()
        '''
		print("Esta es")
		print(root.getValue())
		print(root.getLeft().getValue())
		print(root.getLeft().getLeft().getValue())
		'''
        print("\n POSTORDEN")
        #self.postOrderDirecto(root)
        d.construirFuncionesBasicas(root)
        #return self.pila[0]