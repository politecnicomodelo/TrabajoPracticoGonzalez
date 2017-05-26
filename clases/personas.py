from datetime import date

class persona(object):
    nombre = ""
    apellido = ""
    fecha_nac = date
    DNI = 0

    def agregarPersona(self,nom,ape,fec,dni):
        self.nombre = nom
        self.apellido = ape
        self.fecha_nac = fec
        self.DNI = dni

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getDNI(self):
        return self.DNI

    def getFecha_nac(self):
        return self.fecha_nac