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
entrada = "((((a.((b.a).((b.a)*α)))|((a.(b*α)).a))|(a|b)).#)"
a.armarArbol(entrada)


#(ba)+ = ((b.a).((b.a)*α))
#((a.(b*α)).a)
#(a|b)

