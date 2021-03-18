class NodoDirecto(object):
    def __init__(self,estados,estadoInicial = False):
        self.relaciones = []
        self.estadoFinal = False
        self.estadoInicial = estadoInicial
        self.estados = estados # es lista

    def agregarRelacion(self,nuevaRelacion):
        self.relaciones.append(nuevaRelacion)
    
    def isEstadoFinal(self):
        return self.estadoFinal
    
    def isEstadoInicial(self):
        return self.estadoInicial
    
    def setEstadoFinal(self):
        self.estadoFinal = True
    
    def getRelacionesObjeto(self):
        return self.relaciones
    
    def getRelaciones(self):
        relacionesList = []
        for relacion in self.relaciones:
            relacionesList.append(relacion.getRelacion())
        return relacionesList
    
    def getEstados(self):
        return self.estados
    
            


class RelacionDirecto(object):
    def __init__(self, idNodo1, nombreRelacion, idNodo2):
        self.idNodo1 = idNodo1
        self.nombreRelacion = nombreRelacion
        self.idNodo2 = idNodo2

    def getRelacion(self):
        return [self.idNodo1, self.idNodo2, self.nombreRelacion]
    
    def actualizarRelacion(self,diccionarioId):
        try:
            self.idNodo1 = diccionarioId[self.idNodo1]
            self.idNodo2 = diccionarioId[self.idNodo2]
        except:
            pass


# Funciones complementarias

def getLetraDeEstados(DFA, estados):
    for letra, nodo in DFA.items():
        if(
            list(set(nodo.getEstados()) - set(estados))
            ==
            list(set(estados) - set(nodo.getEstados()))
            ==
            []
        ):
            return letra


def getEstadosFinales(DFA):
    estadosFinales = []
    for id, nodo in DFA.items():
        if (nodo.isEstadoFinal()):
            estadosFinales.append(id)
    
    return estadosFinales

def getEstadosIniciales(DFA):
    estadosFinales = []
    for id, nodo in DFA.items():
        if (nodo.isEstadoInicial()):
            estadosFinales.append(id)
    
    return estadosFinales

def getRelacionesDFA(DFA):
    relaciones = []
    for id, nodo in DFA.items():
        relaciones.append(nodo.getRelaciones())
    return relaciones

def setEstadosFinales(DFA, idHash):
    for id, nodo in DFA.items():
        if (idHash in nodo.getEstados()):
            nodo.setEstadoFinal()
    return DFA

def mover(estado,letra):
    try:
        for i in estado.getRelaciones():
            if (i[2] == letra):
                return i[1]
    except:
        return []
    
    return []