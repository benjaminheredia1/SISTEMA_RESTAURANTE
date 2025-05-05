from persona import Persona

class Empleado(Persona):
    lista_empleados = []

    def __init__(self, idpersona, nombre, cedula, telefono, cargo, salario):
        super().__init__(idpersona, nombre, cedula, telefono)
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.idpersona} - {self.nombre} - {self.cargo} - {self.salario}"

    @classmethod
    def registrar_empleado(cls, empleado):
        cls.lista_empleados.append(empleado)

    @classmethod
    def ordenar_lista_empleados(cls):
        def quicksort(lista):
            if len(lista) <= 1:
                return lista
            pivote = lista[0]
            menores = [x for x in lista[1:] if x.idpersona < pivote.idpersona]
            mayores = [x for x in lista[1:] if x.idpersona >= pivote.idpersona]
            return quicksort(menores) + [pivote] + quicksort(mayores)
        cls.lista_empleados = quicksort(cls.lista_empleados)

    @classmethod
    def obtener_lista_empleados(cls):
        return cls.lista_empleados