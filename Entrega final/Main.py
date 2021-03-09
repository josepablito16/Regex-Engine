from Arbol import *
from Thompson import *


a = Arbol()

#entrada = "(a|b)*abb"
entrada = "(ε|a*b)"
visualizarNFA(a.interpretarEcuacion(entrada))