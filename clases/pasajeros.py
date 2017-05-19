from personas import persona

class pasajero(persona):
    millas = 0
    VIP = False
    necesidadesEsp = ""

    def cambiarMVN(self,mil,vi,nes):
        self.millas = mil
        self.VIP = vi
        self.necesidadesEsp = nes