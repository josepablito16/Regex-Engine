from Arbol import *
from Thompson import *
import Grafo as g
import Subconjuntos as s


a = Arbol()

#entrada = "(a|b)*abb"
#entrada = "(((a.((b.a).((b.a)*α)))|((a.(b*α)).a))|(a|b))"
'''
((1?)*)*    =   (((1|ε)*α)*α)
'''
entrada = "(((1|ε)*α)*α)"


cadena = "1"


NFA = a.interpretarEcuacion(entrada)
#g.visualizarNFA(NFA)
g.visualizarNFD(s.generarSubConjuntos(NFA))


# DFA directo
entrada = f"({entrada}.#)"
#g.visualizarDirecto(a.armarArbol(entrada))


