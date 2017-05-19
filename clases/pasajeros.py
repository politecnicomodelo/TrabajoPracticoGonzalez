from clases.personas import persona

class pasajero(persona):
    VIP = False
    necesidadesEsp = ""

    def cambiarMVN(self,vi,nes):
        self.VIP = vi
        self.necesidadesEsp = nes