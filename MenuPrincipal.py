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
listaTripulacion = []
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
        listaTripulacion.append(unPiloto)

    elif(lista[0] == "Servicio"):
        unServicio = serviciosAbordo()
        lista = item.split('|')
        unServicio.agregarPersona(str(lista[1]), str(lista[2]), lista[3], str(lista[4]))
        unServicio.autorizarModelo(lista[5].split(','))
        unServicio.agregarIdioma(str(lista[6].split(',')))
        listaTripulacion.append(unServicio)

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
        unVuelo.agregarTripulante(lista[6].split(','))
        unVuelo.agregarPasajero(lista[7].split(','))
        listaVuelos.append(unVuelo)

def nominaPasajeros(fecha,hora,modelo):
    verPasajeros = 0
    for vue in listaVuelos:
        if(listaVuelos[vue].getFecha() == fecha && listaVuelos[vue].getHora() == hora && listaVuelos[vue].getModelo() == modelo):
            verPasajeros = listaVuelos[vue].getListaPasajeros()
    for buscar in verPasajeros
        for buscarP in listaPersonas
            if(verPasajeros[buscar] == listaPersonas[buscarP].getDNI()):
                print(listaPersonas[buscarP].getNombre() + " " + listaPersonas[buscarP].getApellido() + " " + listaPersonas[buscarP].getDNI())

def pasajeroJoven(fecha,hora,modelo):
    verPasajeros = 0
    for vue in listaVuelos:
        if (listaVuelos[vue].getFecha() == fecha && listaVuelos[vue].getHora() == hora && listaVuelos[vue].getModelo() == modelo):
            verPasajeros = listaVuelos[vue].getListaPasajeros()
    for buscar in verPasajeros
        pasajeroMasJoven = pasajero()
        if(verPasajeros[buscar].getFecha_nac() > pasajeroMasJoven.getFecha_nac()):
            pasajeroMasJoven = verPasajeros[buscar]

def tripulacionMinima(fecha,hora,modelo):
    verPasajeros = 0
    cantidadTripulacion = 0
    for vue in listaVuelos:
        if (listaVuelos[vue].getFecha() == fecha && listaVuelos[vue].getHora() == hora && listaVuelos[vue].getModelo() == modelo):
            verPasajeros = listaVuelos[vue].getListaTripulacioon()
    for buscar in listaAviones:
        if(listaAviones[buscar].getModelo == modelo):
            if(listaAviones[buscar].getTripMin >= len(verPasajeros)):
                print("hay sufucuente tripulacion")
            else:
                print("no hay suficiente tripulacion para este vuelo")

def personasAutorizadas(fecha,hora,modelo):
    todoBien = True
    verPasajeros = 0
    for vue in listaVuelos:
        if (listaVuelos[vue].getFecha() == fecha && listaVuelos[vue].getHora() == hora && listaVuelos[vue].getModelo() == modelo):
            verPasajeros = listaVuelos[vue].getListaTripulacioon()
    for pervue in listaTripulacion:
        for per in verPasajeros:
            if(listaTripulacion[pervue].getDNI == verPasajeros[per].getDNI):
                listaAutorizados = verPasajeros[per].getModelosAutorizados
                for modaut in listaAutorizados:
                    if(listaAutorizados[modaut] != modelo):
                        todoBien = False
    if(todoBien == True):
        print("Todo bien,Todo correcto y yo que me alegro")
    else:
        print("Un tripulante no esta autorizado")

def NoMasVuelos(fecha,hora,modelo):
    vuelosTripulante = []
    verPasajeros = listaTripulacion
    for trivue in verPasajeros:
        TripulantePorVuelo = []
        solo = False
        for vuetri in listaVuelos:
            vuelosTripulante = listaVuelos[vuetri].getlistaTripulantes
            for vuetri2 in vuelosTripulante:
                if(verPasajeros[vue].getDNI == vuelosTripulante[vuetri2]):
        for busfec in TripulantePorVuelo:
            for busbus in TripulantePorVuelo:
                if (busbus == busfec):
                    continue
                if(TripulantePorVuelo[busfec] == TripulantePorVuelo[busbus]):
                    solo = True
        if(solo == True):
            print("tripulante: " + verPasajeros[trivue].getDNI + " esta infringiendo la regla de vuelo por dia")

def PersonasVueloVIP(fecha,hora,modelo):
    verPersonas = listaPersonas
    verVuelos = listaVuelos
    verPersonasVIP = []
    for perVIP in verPersonas:
        if(verPersonas[perVIP].getVIP == True):
            verPersonasVIP.append(verPersonas[perVIP])
