from Arbol import *
from Thompson import *
import Grafo as g


a = Arbol()

#entrada = "(a|b)*abb"
entrada = "(ε|a*b)"
g.visualizarNFA(a.interpretarEcuacion(entrada))