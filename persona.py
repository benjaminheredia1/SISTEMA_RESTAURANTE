class Persona:
    def __init__(self,idpersona,nombre, cedula, telefono):
        self.idpersona = idpersona
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Cédula: {self.cedula}, Teléfono: {self.telefono}"