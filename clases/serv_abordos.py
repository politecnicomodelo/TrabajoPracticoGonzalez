from tripulacion import tripulacion

class serviciosAbordo(tripulacion):
    idiomas = []

    def autorizarModelo(self, mod):
        self.modelosAutorizados.append(mod)

    def agregarIdioma(self,idi):
        self.idiomas.append(idi)

