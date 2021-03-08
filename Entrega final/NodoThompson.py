class NodoThompson(object):
    def __init__(self, estadoInicial, estadoFinal):
        self.relaciones = []
        self.estadoFinal = estadoFinal
        self.estadoInicial = estadoInicial

    def agregarRelacion(self,nuevaRelacion):
        self.relaciones.append(nuevaRelacion)
    
    def isEstadoFinal(self):
        return self.estadoFinal
    
    def isEstadoInicial(self):
        return self.estadoInicial
    
    def getRelaciones(self):
        relacionesList = []
        for relacion in self.relaciones:
            relacionesList += relacion.getRelacion()
        return relacionesList


class RelacionThompson(object):
    def __init__(self, idNodo1, nombreRelacion, idNodo2):
        self.idNodo1 = idNodo1
        self.nombreRelacion = nombreRelacion
        self.idNodo2 = idNodo2

    def getRelacion(self):
        return [self.idNodo1, self.idNodo2, self.nombreRelacion]


def getEstadosFinales(NFA):
    estadosFinales = []
    for id, nodo in NFA.items():
        if (nodo.isEstadoFinal()):
            estadosFinales.append(id)
    return estadosFinales

def getRelacionesNFA(NFA):
    relaciones = []
    for id, nodo in NFA.items():
        relaciones.append(nodo.getRelaciones())
    
    return relaciones