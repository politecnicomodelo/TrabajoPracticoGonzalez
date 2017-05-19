from vuelos import vuelo
from pasajeros import pasajero
from pilotos import piloto
from serv_abordos import serviciosAbordo
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

    def agregarPasajero(self,nom,ape,fec,dni,mil,vi,nes):
        unPasajero = pasajero
        unPasajero.agregarPersona(nom,ape,fec,dni)
        unPasajero.cambiarMVN(mil,vi,nes)
        self.listaPasajeros.append(unPasajero)

    def agregarPiloto(self,nom,ape,fec,dni,mod):
        unPiloto = piloto
        unPiloto.agregarPersona(nom,ape,fec,dni)
        unPiloto.autorizarModelo(mod)
        self.listaTripulacion.append(unPiloto)

    def agregarServicioAbordo(self,nom,ape,fec,dni,mod,idi):
        unServicio = serviciosAbordo
        unServicio.agregarPersona(nom,ape,fec,dni)
        unServicio.autorizarModelo(mod)
        unServicio.agregarIdioma(idi)
        self.listaTripulacion.append(unServicio)

    def modificarVuelo(self,mod,fec,hor,ori,des):
        self.modelo = mod
        self.fecha = fec
        self.hora = hor
        self.origen = ori
        self.destino = des