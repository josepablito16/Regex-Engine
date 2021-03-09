from Nodo import Node
from itertools import product
from Preprocesador import preProcesarExpresion
import numpy as np
from Thompson import *


class Arbol(object):
    """docstring for Arbol"""

    def __init__(self):
        self.pila = []
        self.operadores = ['|', '*','.']
        self.numeros = ['a', 'b','ε']
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

                self.pila.append(construirOr(NFA1, NFA2))

            if(Node.getValue() == '*'):
                NFA1 = self.pila[len(self.pila)-1]
                NFA2 = self.pila[len(self.pila)-2]

                

                self.pila.pop()
                self.pila.pop()
                #print(f"{num1} - {num2}")

                self.pila.append(construirKleen(NFA2))


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

                self.pila.append(construirConcatenacion(NFA2, NFA1))

            if(Node.getValue() == '^'):
                num1 = self.pila[len(self.pila)-1]
                num2 = self.pila[len(self.pila)-2]

                self.pila.pop()
                self.pila.pop()
                #print(f"{num1} / {num2}")

                self.pila.append(self.exp(float(num1), float(num2)))

        else:
            print(f"No Operador {Node.getValue()}")
            self.pila.append(construirUnSimbolo(Node.getValue()))
        # print("ECUACION")
        # print(self.ecuacion)

    def interpretarEcuacion(self, entrada):
        entrada = preProcesarExpresion(entrada)
        print(entrada)
        root = Node(None)
        actual = root

        for i in entrada:
            if(i == '('):
                actual.setLeft(None, actual)
                actual = actual.getLeft()

            if(i in self.operadores):
                actual.setValue(i)
                actual.setRight(None, actual)
                actual = actual.getRight()

            if(i in self.numeros):
                actual.setValue(i)
                actual = actual.getRoot()

            if(i == ')'):
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