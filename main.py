
"""
from cliente import Cliente  # Importa la clase desde cliente.py

# Crear un cliente
cliente1 = Cliente(1, "Laura Pérez", "45434", "laura@example.com")

# Registrar una visita
cliente1.registrar_visita()

# Agregar un pedido
cliente1.agregar_pedido("Pizza Margarita")

# Mostrar información

print("------ CLIENTE REGISTRADO ------ ")
print(cliente1.nombre)
print(cliente1.obtener_historial_pedidos())
"""

def mostrar_menuOpciones():
    print("\n[========= RESTAURANTE ""PORVENIR"" =========]")
    print("1. Ver menú de comida")
    print("2. Agregar pedido")
    print("3. Ver cuenta")
    print("4. Salir")

def ver_menu_comida():
    print("\n--- MENÚ DE COMIDA ---")
    for item, precio in menu.items():
        print(f"{item}: ${precio}")

def agregar_pedido():
    ver_menu_comida()
    pedido = input("¿Qué desea pedir? (escriba el nombre del platillo): ")
    if pedido in menu:
        cuenta.append(pedido)
        print(f"{pedido} agregado a su pedido.")
    else:
        print("Ese platillo no está en el menú.")

def ver_cuenta():
    print("\n--- SU CUENTA ---")
    total = 0
    for item in cuenta:
        print(f"{item}: ${menu[item]}")
        total += menu[item]
    print(f"Total a pagar: ${total}")

# Datos del restaurante
menu = {
    "Hamburguesa": 8.50,
    "Pizza": 12.00,
    "Ensalada": 6.00,
    "Refresco": 2.50,
    "Café": 3.00
}

cuenta = []

# --- Menu de opciones
print("Bienvenido/a!!")
salirprograma = True;
while salirprograma:
    mostrar_menuOpciones()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        ver_menu_comida()
    elif opcion == "2":
        agregar_pedido()
    elif opcion == "3":
        ver_cuenta()
    elif opcion == "4":
        print("Gracias por su visita. ¡Hasta luego!")
        salirprograma = False
    else:
        print("Opción inválida. Intente de nuevo.")
