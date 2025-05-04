import persona
class Empleado:
    class Empleado(persona):
        def __init__(self,idempleado, nombre, cedula, telefono, cargo, salario):
            super().__init__(idempleado,nombre, cedula, telefono)
            self.cargo = cargo
            self.salario = salario

    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"{base_info}, Cargo: {self.cargo}, Salario: ${self.salario:.2f}"