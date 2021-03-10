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
