from .aviones import avion
from .pasajeros import pasajero
from .pilotos import piloto
from .serv_abordos import serviciosAbordo
from _datetime import date
from _datetime import time

class vuelo(object):
    modelo = ""
    listaPasajeros = []
    listaTripulacion = []
    fecha = date
    hora = time
    origen = ""
    destino = ""

    def agregarPasajero(self,dni):
        self.listaPasajeros.append(dni)

    def agregarTripulante(self,dni):
        self.listaTripulacion.append(dni)

    def modificarVuelo(self,mod,fec,hor,ori,des):
        self.modelo = mod
        self.fecha = fec
        self.hora = hor
        self.origen = ori
        self.destino = des
