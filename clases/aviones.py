class avion(object):
    modelo = ""
    cantidadPasajeros = 0
    cantidadTripulacion = 0

    def agregarAvion(self,mod,cpa,ctr):
        self.modelo = mod
        self.cantidadPasajeros = cpa
        self.cantidadTripulacion = ctr