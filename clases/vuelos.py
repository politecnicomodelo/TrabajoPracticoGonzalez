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

