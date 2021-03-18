class NodoSubconjuntos(object):
    def __init__(self, estadoInicial, estados):
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
    
            


class RelacionSubconjuntos(object):
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
def getEstadosFinales(NFD):
    estadosFinales = []
    for id, nodo in NFD.items():
        if (nodo.isEstadoFinal()):
            estadosFinales.append(id)
    
    return estadosFinales

def getEstadosIniciales(NFD):
    estadosIniciales = []
    for id, nodo in NFD.items():
        if (nodo.isEstadoInicial()):
            estadosIniciales.append(id)
    
    return estadosIniciales

def setEstadosFinales(NFD, idEstadoFinal):
    for id, nodo in NFD.items():
        if (idEstadoFinal in nodo.getEstados()):
            nodo.setEstadoFinal()
    
    return NFD

def getRelacionesNFD(NFD):
    relaciones = []
    for id, nodo in NFD.items():
        relaciones.append(nodo.getRelaciones())
    return relaciones


def printNFDdebug(NFD):
    for id, nodo in NFD.items():
        print(f"{id} : {nodo.getEstados()}")

def mover(estado,letra):
    try:
        for i in estado.getRelaciones():
            if (i[2] == letra):
                return i[1]
    except:
        return []
    
    return []

