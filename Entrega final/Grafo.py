from graphviz import Digraph
from NodoThompson import *
'''
f = Digraph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')

f.attr('node', shape='doublecircle')
f.node('LR_0')
f.node('LR_3')
f.node('LR_4')
f.node('LR_8')

f.attr('node', shape='circle')
f.edge('LR_0', 'LR_2', label='SS(B)')
f.edge('LR_0', 'LR_1', label='SS(S)')
f.edge('LR_1', 'LR_3', label='S($end)')
f.edge('LR_2', 'LR_6', label='SS(b)')
f.edge('LR_2', 'LR_5', label='SS(a)')
f.edge('LR_2', 'LR_4', label='S(A)')
f.edge('LR_5', 'LR_7', label='S(b)')
f.edge('LR_5', 'LR_5', label='S(a)')
f.edge('LR_6', 'LR_6', label='S(b)')
f.edge('LR_6', 'LR_5', label='S(a)')
f.edge('LR_7', 'LR_8', label='S(b)')
f.edge('LR_7', 'LR_5', label='S(a)')
f.edge('LR_8', 'LR_6', label='S(b)')
f.edge('LR_8', 'LR_5', label='S(a)')

f.view()
'''

def visualizarNFA(NFA):
    f = Digraph('finite_state_machine', filename='fsm.gv')
    f.attr(rankdir='LR', size='8,5')

    # Estados finales
    f.attr('node', shape='doublecircle')
    
    print("ESTADOS FINALES")
    for idNodo in getEstadosFinales(NFA):
        f.node(str(idNodo))
        print(idNodo)
    
    print("RELACIONES")
    f.attr('node', shape='circle')
    for relacion in getRelacionesNFA(NFA):
        try:
            
            if len(relacion) > 1:
                for subRelacion in relacion:
                    print(subRelacion)
                    f.edge(str(subRelacion[0]), str(subRelacion[1]), label=str(subRelacion[2]))
            else:
                print(relacion)
                f.edge(str(relacion[0][0]), str(relacion[0][1]), label=str(relacion[0][2]))
        except:
            pass

    f.view()
    '''
    f.edge('LR_0', 'LR_1', label='SS(S)')
    f.edge('LR_1', 'LR_3', label='S($end)')
    f.edge('LR_2', 'LR_6', label='SS(b)')
    f.edge('LR_2', 'LR_5', label='SS(a)')
    f.edge('LR_2', 'LR_4', label='S(A)')
    f.edge('LR_5', 'LR_7', label='S(b)')
    f.edge('LR_5', 'LR_5', label='S(a)')
    f.edge('LR_6', 'LR_6', label='S(b)')
    f.edge('LR_6', 'LR_5', label='S(a)')
    f.edge('LR_7', 'LR_8', label='S(b)')
    f.edge('LR_7', 'LR_5', label='S(a)')
    f.edge('LR_8', 'LR_6', label='S(b)')
    f.edge('LR_8', 'LR_5', label='S(a)')

    '''
