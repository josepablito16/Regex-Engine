from Arbol import *
from Thompson import *
import Grafo as g
import Subconjuntos as s


a = Arbol()

#entrada = "(a|b)*abb"
entrada = "(ε|a*b)"

NFA = a.interpretarEcuacion(entrada)
g.visualizarNFA(NFA)
g.visualizarNFD(s.generarSubConjuntos(NFA))


# DFA directo
a.armarArbol(entrada)
