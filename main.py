import os
from empleado import Empleado
# --- metodos de accion principal
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menuOpciones(tipousuario):
    print("\n[========= RESTAURANTE ""PORVENIR"" =========]")
    if tipousuario == "administrador":
        print("1. registrar empleado")
        print("4. Salir")
    elif tipousuario == "empleado":
        print("1. atender perdido")
        print("4. Salir")

# --- funciones del menu opciones
def registraOrdenarEmpleado():
    e1 = Empleado(1, "Juan", "123456", "789456", "Contador", 5000)
    e2 = Empleado(2, "Ana", "987654", "123789", "Ingeniera", 6000)
    e3 = Empleado(3, "Luis", "456789", "654321", "Analista", 5500)

    Empleado.registrar_empleado(e1)
    Empleado.registrar_empleado(e2)
    Empleado.registrar_empleado(e3)

    Empleado.ordenar_lista_empleados()

    print("Lista ordenada de empleados:")
    for emp in Empleado.obtener_lista_empleados():
        print(emp)


# lista de usuarios para acceder al sistema
usuarios = [
    {"usuario": "admin", "contrasena": "123", "tipo": "administrador"},
    {"usuario": "carlos", "contrasena": "321", "tipo": "empleado"}
]

# funcion para simular login
def login(usuario, contrasena):
    for user in usuarios:
        if user["usuario"] == usuario and user["contrasena"] == contrasena:
            limpiar_pantalla()
            print("Bienvenido/a, " + user['usuario'] +"")
            # --- Menu de opciones
            while True:
                mostrar_menuOpciones(user['tipo'])
                opcion = input("Seleccione una opción (1-4): ")

                while True:
                    if user['tipo'] == "administrador":
                        if opcion == "1":
                            limpiar_pantalla()
                            registraOrdenarEmpleado()
                        elif opcion == "4":
                            limpiar_pantalla()
                            print("Gracias por su visita. ¡Hasta luego!")
                            exit()
                            break
                        else:
                            print("Opción inválida. Intente de nuevo.")
                            break
                    elif user['tipo'] == "empleado":
                        if opcion == "1":
                            limpiar_pantalla()
                            print("Atender pedido")
                        elif opcion == "4":
                            limpiar_pantalla()
                            print("Gracias por su visita. ¡Hasta luego!")
                            exit()
                            break
                        else:
                            print("Opción inválida. Intente de nuevo.")
                            break
                        
                    continuar = input("Escriba 'ok' para volver al menú o cualquier otra tecla para repetir esta opción: ").lower()
                    if continuar == 'ok':
                        break


# --- inicio del programa
respuesta = True

while  respuesta == True:
    print("\n|================= BIENVENIDO AL RESTAURANTE ""PORVENIR"" =================|")
    usuario = input("| Ingrese su nombre de usuario: ")
    contrasena = input("| Ingrese su contraseña: ")
    login(usuario, contrasena)

