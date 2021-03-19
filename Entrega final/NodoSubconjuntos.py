class NodoSubconjuntos(object):
    """
    Este objeto guarda toda la informacion de un nodo
    especificamente para el algoritmo de generacion
    de subconjuntos

    Variable
    ----------
    relaciones : list
        guarda una lista de objetos relacion del nodo
    estadoFinal : Bool
        es estado final?
    estadoInicial : Bool
        es estado inicial?
    estados : lsit
        ids de todos los estados que representa el nodo
    """
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
    """
    Este objeto guarda toda la informacion de una relacion
    especificamente para el algoritmo directo

    Variable
    ----------
    idNodo1 : int
        id del nodo que posee la relacion
    nombreRelacion : str
        texto de la transicion de la relacion
    idNodo2 : int
        id del nodo a que se llega con la relacion
    """
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

