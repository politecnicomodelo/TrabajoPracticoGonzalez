from tripulacion import tripulacion

class piloto(tripulacion):

    def autorizarModelo(self,mod):
        self.modelosAutorizados.append(mod)