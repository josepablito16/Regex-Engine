from Nodo import Node
from itertools import product
from Preprocesador import preProcesarExpresion
import numpy as np


class Arbol(object):
    """docstring for Arbol"""

    def __init__(self):
        self.ecuacion = []
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
            if(Node.getValue() == '+'):
                num1 = self.ecuacion[len(self.ecuacion)-1]
                num2 = self.ecuacion[len(self.ecuacion)-2]

                self.ecuacion.pop()
                self.ecuacion.pop()
                #print(f"{num1} + {num2}")

                self.ecuacion.append(self.suma(float(num1), float(num2)))

            if(Node.getValue() == '-'):
                num1 = self.ecuacion[len(self.ecuacion)-1]
                num2 = self.ecuacion[len(self.ecuacion)-2]

                self.ecuacion.pop()
                self.ecuacion.pop()
                #print(f"{num1} - {num2}")

                self.ecuacion.append(self.resta(float(num1), float(num2)))


            if(Node.getValue() == '/'):
                num1 = self.ecuacion[len(self.ecuacion)-1]
                num2 = self.ecuacion[len(self.ecuacion)-2]

                self.ecuacion.pop()
                self.ecuacion.pop()
                #print(f"{num1} / {num2}")

                self.ecuacion.append(self.div(float(num1), float(num2)))

            if(Node.getValue() == '^'):
                num1 = self.ecuacion[len(self.ecuacion)-1]
                num2 = self.ecuacion[len(self.ecuacion)-2]

                self.ecuacion.pop()
                self.ecuacion.pop()
                #print(f"{num1} / {num2}")

                self.ecuacion.append(self.exp(float(num1), float(num2)))

        else:
            print(f"No Operador {Node.getValue()}")
            self.ecuacion.append(Node.getValue())
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
        return self.ecuacion[0]