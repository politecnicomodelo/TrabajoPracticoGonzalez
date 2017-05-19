from clases.personas import persona

class tripulacion(persona):
    modelosAutorizados = []

    def autorizarModelo(self,mod):
        self.modelosAutorizados.append(mod)
