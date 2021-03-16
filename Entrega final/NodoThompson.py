class NodoThompson(object):
    def __init__(self, estadoInicial, estadoFinal):
        self.relaciones = []
        self.estadoFinal = estadoFinal
        self.estadoInicial = estadoInicial

    def agregarRelacion(self,nuevaRelacion):
        self.relaciones.append(nuevaRelacion)
    
    def setRelaciones(self, relacionesObjeto):
        self.relaciones = relacionesObjeto
    
    def isEstadoFinal(self):
        return self.estadoFinal
    
    def isEstadoInicial(self):
        return self.estadoInicial
    
    def clearEstado(self):
        self.estadoFinal = False
        self.estadoInicial = False
    
    def setEstados(estadoInicial, estadoFinal):
        self.estadoFinal = estadoFinal
        self.estadoInicial = estadoInicial
    
    def getRelacionesObjeto(self):
        return self.relaciones
    
    def getRelaciones(self):
        relacionesList = []
        for relacion in self.relaciones:
            relacionesList.append(relacion.getRelacion())
        return relacionesList
    
    def actualizarRelaciones(self, diccionarioId):
        for relacion in self.relaciones:
            relacion.actualizarRelacion(diccionarioId)
            


class RelacionThompson(object):
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


# METODOS COMPLEMENTARIOS
def getEstadosFinales(NFA):
    estadosFinales = []
    for id, nodo in NFA.items():
        if (nodo.isEstadoFinal()):
            estadosFinales.append(id)
    return estadosFinales

def getEstadosIniciales(NFA):
    estadosIniciales = []
    for id, nodo in NFA.items():
        if (nodo.isEstadoInicial()):
            estadosIniciales.append(id)
    return estadosIniciales

def getRelacionesNFA(NFA):
    relaciones = []
    for id, nodo in NFA.items():
        relaciones.append(nodo.getRelaciones())
    return relaciones


def actualizarIdsNodos(NFA, idContador):
    diccionarioId = {}
    nuevoNFA = {}
    for idViejo, nodoViejo in NFA.items():
        diccionarioId[idViejo] = idContador + 1
        nuevoNFA[diccionarioId[idViejo]] = nodoViejo
        idContador += 1
    
    for idViejo, nodoViejo in nuevoNFA.items():
        nodoViejo.actualizarRelaciones(diccionarioId)
    
    return nuevoNFA, idContador


def getIdInicial(NFA):
    for id, nodo in NFA.items():
        if (nodo.isEstadoInicial()):
            nodo.clearEstado()
            return id, NFA

def getIdFinal(NFA):
    for id, nodo in NFA.items():
        if (nodo.isEstadoFinal()):
            nodo.clearEstado()
            return id, NFA

def actualizarRelacionConcatenacion(NFA, idNodo1, idNodo2):
    for id, nodo in NFA.items():
        try:
            nodo.actualizarRelaciones({idNodo2 : idNodo1})
        except:
            pass
    return NFA


def mergeEstados(NFA, idNodo1, idNodo2):
    # Dejar id de nodo1
    # Dejar relaciones de nodo2

    NFAnuevo={}

    for id, nodo in NFA.items():
        if (id == idNodo1 or id == idNodo2):
            pass
        else:
            NFAnuevo[id] = nodo
    
    NFAnuevo[idNodo1] = NodoThompson(False, False)
    NFAnuevo[idNodo1].setRelaciones(NFA[idNodo2].getRelacionesObjeto())

    NFAnuevo = actualizarRelacionConcatenacion(NFAnuevo, idNodo1, idNodo2)

    return NFAnuevo







    

    
