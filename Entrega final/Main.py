from Arbol import *
import Thompson as t
import Grafo as g
import Subconjuntos as s


a = Arbol()

#entrada = "(a|b)*abb"
#entrada = "(((a.((b.a).((b.a)*α)))|((a.(b*α)).a))|(a|b))"
'''
(a|b)*a(a|b)(a|b)+  =   (((((a|b)*α).a).(a|b)).(((a|b)*α).(a|b)))
((1?)*)*    =   (((1|ε)*α)*α)
(a|ε)b(a+)c?    =   ((((a|ε).b).((a*α).a)).(c|ε))
(1|0)+001   =   ((((((1|0)*α).(1|0)).0).0).1)
(εa|εb)*abb =   ((((((ε.a)|(ε.b))*α).a).b).b)
'''
entrada = "(((1|ε)*α)*α)"

cadena = "abc"


NFA = a.interpretarEcuacion(entrada)
print(f"Simulacion NFA = {t.simularNFA(NFA, cadena)}")

#g.visualizarNFA(NFA)
#g.visualizarNFD(s.generarSubConjuntos(NFA))


# DFA directo
entrada = f"({entrada}.#)"
#g.visualizarDirecto(a.armarArbol(entrada))


