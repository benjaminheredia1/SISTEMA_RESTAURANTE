
class Cliente:
    def __init__(self, id_cliente: int, nombre: str, telefono: str, correo: str):
        self.id = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.visitas = 0
        self.pedidos = []

    def registrar_visita(self):
        self.visitas += 1

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def obtener_historial_pedidos(self):
        return self.pedidos
