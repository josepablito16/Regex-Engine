from Arbol import *
import Thompson as t
import Grafo as g
import Subconjuntos as s
import Directo as d
import Preprocesador as p
import time
import sys

'''
Main del proyecto, se utilizan todos
los scripts del proyecto para construir y simular
NFA, NFD y DFA. Utilizando algoritmos de Thompson, 
generacion de subconjuntos y directo
'''

a = Arbol()

#entrada = "(a|b)*abb"
#entrada = "(((a.((b.a).((b.a)*α)))|((a.(b*α)).a))|(a|b))"
'''
(a|b)*a(a|b)(a|b)+  =   (((((a|b)*α).a).(a|b)).(((a|b)*α).(a|b)))
((1?)*)*    =   (((1|ε)*α)*α)
(a|ε)b(a+)c?    =   ((((a|ε).b).((a*α).a)).(c|ε))
(1|0)+001   =   ((((((1|0)*α).(1|0)).0).0).1)
(εa|εb)*abb =   ((((((ε.a)|(ε.b))*α).a).b).b)

CON ERRORES
(a|b*a(a|b)(a|b)+   =   ((((a|(b*α).a).(a|b)).(((a|b)*α).(a|b)))
((1?)** =   ((1|ε)**
(a|ε)b(a+c? =   ((((a|ε).b).((a*α).a).(c|ε))
(εa|εb)*ab)b    =   (((((ε.a)|(ε.b))*α).a.b)).b)
(a-b)
(a.(a/b))
'''
entrada = input("Escriba una expresion regular: ")

cadena = input("Ingresa la palabra a validar: ")


if (p.isError(entrada)):

    sys.exit()

print(f'''
    Expr = {entrada}
    Cadena = {cadena}
''')

# NFA
NFA = a.interpretarEcuacion(entrada)
start_time = time.time()
print(f"""
    Simulacion NFA = {t.simularNFA(NFA, cadena)}
    Tiempo simulacion NFA = {(time.time() - start_time)}
    """)
g.visualizarNFA(NFA)

# NFD
NFD = s.generarSubConjuntos(NFA)
start_time = time.time()
print(f"""
    Simulacion NFD = {s.simularNFD(NFD, cadena)}
    Tiempo simulacion NFD = {(time.time() - start_time)}
    """)
g.visualizarNFD(NFD)


# DFA directo
entrada = f"({entrada}.#)"
DFA_directo = d.construirFuncionesBasicas(a.armarArbol(entrada))

start_time = time.time()
print(f"""
    Simulacion DFA = {d.simularDirecto(DFA_directo, cadena)}
    Tiempo simulacion DFA = {(time.time() - start_time)}
    """)
g.visualizarDirecto(DFA_directo)



