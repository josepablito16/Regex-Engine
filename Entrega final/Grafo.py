from graphviz import Digraph
import NodoThompson as nt
import NodoSubconjuntos as ns
import NodoDirecto as nd

'''
Script para graficar todos los grafos
NFA, NFD y DFA
'''

def visualizarNFA(NFA, nombre="NFA_Actual"):
    f = Digraph('finite_state_machine', filename=f'{nombre}.gv')
    f.attr(rankdir='LR', size='8,5')

    estadosIniciales = nt.getEstadosIniciales(NFA)

    # Estados finales
    f.attr('node', shape='doublecircle')
    
    for idNodo in nt.getEstadosFinales(NFA):
        f.node(str(idNodo))
    

    f.attr('node', shape='circle')
    
    # Estados iniciales
    for i in estadosIniciales:
        f.node(str(i), color="#3F888F")

    for relacion in nt.getRelacionesNFA(NFA):
        try:
            
            if len(relacion) > 1:
                for subRelacion in relacion:
                    f.edge(str(subRelacion[0]), str(subRelacion[1]), label=str(subRelacion[2]))
            else:
                f.edge(str(relacion[0][0]), str(relacion[0][1]), label=str(relacion[0][2]))
        except:
            pass

    f.view()


def visualizarNFD(NFD, nombre="NFD_Actual"):
    f = Digraph('finite_state_machine', filename=f'{nombre}.gv')
    f.attr(rankdir='LR', size='8,5')

    # Estados finales
    f.attr('node', shape='doublecircle')


    estadosIniciales = ns.getEstadosIniciales(NFD)
    
    for idNodo in ns.getEstadosFinales(NFD):
        f.node(str(idNodo))
       
    
   
    f.attr('node', shape='circle')

    # Estados iniciales
    for i in estadosIniciales:
        f.node(str(i), color="#3F888F")

    for relacion in ns.getRelacionesNFD(NFD):
        try:
            
            if len(relacion) > 1:
                for subRelacion in relacion:
                    
                    f.edge(str(subRelacion[0]), str(subRelacion[1]), label=str(subRelacion[2]))
            else:
            
                f.edge(str(relacion[0][0]), str(relacion[0][1]), label=str(relacion[0][2]))
        except:
            pass

    f.view()

def visualizarDirecto(DFA, nombre="DFA_Directo_Actual"):
    f = Digraph('finite_state_machine', filename=f'{nombre}.gv')
    f.attr(rankdir='LR', size='8,5')

    # Estados finales
    f.attr('node', shape='doublecircle')

    estadosIniciales = nd.getEstadosIniciales(DFA)
    
    for idNodo in nd.getEstadosFinales(DFA):
        f.node(str(idNodo))    

    
    f.attr('node', shape='circle')
    
    # Estados iniciales
    for i in estadosIniciales:
        f.node(str(i), color="#3F888F")

    for relacion in nd.getRelacionesDFA(DFA):
        try:
            
            if len(relacion) > 1:
                for subRelacion in relacion:
                    
                    f.edge(str(subRelacion[0]), str(subRelacion[1]), label=str(subRelacion[2]))
            else:
                
                f.edge(str(relacion[0][0]), str(relacion[0][1]), label=str(relacion[0][2]))
        except:
            pass

    f.view()
