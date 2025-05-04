import persona

class Cliente(persona):
    def __init__(self, idcliente: int, nombre: str, cedula: str, telefono: str, correo: str):
        super().__init__(idcliente,nombre, cedula, telefono)
        self.correo = correo
        self.pedidos = []


    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def obtener_historial_pedidos(self):
        return self.pedidos
