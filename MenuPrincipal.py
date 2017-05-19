from clases.vuelos import vuelo
from clases.pasajeros import pasajero
from clases.pilotos import piloto
from clases.serv_abordos import serviciosAbordo
from clases.aviones import avion
from _datetime import date
from _datetime import time

listaVuelos = []
listaAviones = []
listaPersonas = []
listaPilotos = []
listaServicios = []
personas = open("personas.dat","r")
lista = []
for item in personas:
    lista = item.split('|')
    if(item == " "):
        break

    elif(lista[0] == "Pasajero"):
        unPasajero = pasajero()
        lista = item.split('|')
        unPasajero.agregarPersona(str(lista[1]),str(lista[2]),lista[3],str(lista[4]))
        unPasajero.cambiarMVN(lista[5],str(lista[6]))
        listaPersonas.append(unPasajero)

    elif(lista[0] == "Piloto"):
        unPiloto = piloto()
        lista = item.split('|')
        unPiloto.agregarPersona(str(lista[1]),str(lista[2]),lista[3],str(lista[4]))
        unPiloto.autorizarModelo(lista[5].split(','))
        listaPilotos.append(unPiloto)

    elif(lista[0] == "Servicio"):
        unServicio = serviciosAbordo()
        lista = item.split('|')
        unServicio.agregarPersona(str(lista[1]), str(lista[2]), lista[3], str(lista[4]))
        unServicio.autorizarModelo(lista[5].split(','))
        unServicio.agregarIdioma(str(lista[6].split(',')))
        listaServicios.append(unServicio)

aviones = open("aviones.dat","r")
lista2 = []
for item in aviones:
    if(item == " "):
        break

    else:
        unAvion = avion()
        lista2 = item.split('|')
        unAvion.agregarAvion(str(lista2[1]),lista2[2],lista2[3])
        listaAviones.append(unAvion)

vuelos = open("vuelos.dat","r")
lista3 = []
for item in vuelos:
    if(item == " "):
        break

    else:
        unVuelo = vuelo()
        lista3 = item.split('|')
        unVuelo.modificarVuelo(str(lista3[1]),lista3[2],lista3[3],str(lista3[4]),str(lista3[5]))
        unVuelo.agregarPasajero(lista[6].split(','))
        unVuelo.agregarTripulante(lista[7].split(','))
        listaVuelos.append(unVuelo)