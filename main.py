from cliente import Cliente  # Importa la clase desde cliente.py

# Crear un cliente
cliente1 = Cliente(1, "Laura Pérez", "45434", "laura@example.com")

# Registrar una visita
cliente1.registrar_visita()

# Agregar un pedido
cliente1.agregar_pedido("Pizza Margarita")

# Mostrar información
print(cliente1)
print(cliente1.obtener_historial_pedidos())