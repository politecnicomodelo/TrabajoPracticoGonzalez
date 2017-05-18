from tripulacion import tripulacion

class piloto(tripulacion):

    def agregarPiloto(self,nom,ape,fec,dni):
        self.nombre = nom
        self.apellido = ape
        self.fecha_nac = fec
        self.DNI = dni

    def autorizarModelo(self,mod):
        self.modelosAutorizados.append(mod)