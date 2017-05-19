from clases.tripulacion import tripulacion

class serviciosAbordo(tripulacion):
    idiomas = []

    def agregarIdioma(self,idi):
        self.idiomas.append(idi)

