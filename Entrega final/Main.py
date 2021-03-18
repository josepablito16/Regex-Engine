from Arbol import *
import Thompson as t
import Grafo as g
import Subconjuntos as s
import Directo as d


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

cadena = "1"

# NFA
NFA = a.interpretarEcuacion(entrada)
#print(f"Simulacion NFA = {t.simularNFA(NFA, cadena)}")
#g.visualizarNFA(NFA)

# NFD
NFD = s.generarSubConjuntos(NFA)
#print(s.simularNFD(NFD, cadena))
#g.visualizarNFD(NFD)


# DFA directo
entrada = f"({entrada}.#)"
DFA_directo = d.construirFuncionesBasicas(a.armarArbol(entrada))
print(d.simularDirecto(DFA_directo, cadena))
#g.visualizarDirecto(DFA_directo)



