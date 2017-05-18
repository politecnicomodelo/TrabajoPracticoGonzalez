from personas import persona

class pasajero(persona):
    millas = 0
    VIP = False
    necesidadesEsp = ""

    def agregarPasajero(self,nom,ape,fec,dni):
        self.nombre = nom
        self.apellido = ape
        self.fecha_nac = fec
        self.DNI = dni

    def cambiarMVN(self,mil,vi,nes):
        self.millas = mil
        self.VIP = vi
        self.necesidadesEsp = nes