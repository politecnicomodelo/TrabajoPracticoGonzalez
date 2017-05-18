from tripulacion import tripulacion

class serviciosAbordo(tripulacion):
    idiomas = []

    def agregarServ(self, nom, ape, fec, dni):
        self.nombre = nom
        self.apellido = ape
        self.fecha_nac = fec
        self.DNI = dni

    def autorizarModelo(self, mod):
        self.modelosAutorizados.append(mod)

    def agregarIdioma(self,idi):
        self.idiomas.append(idi)

