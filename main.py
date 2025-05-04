import os
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

# lista de usuarios para acceder al sistema
usuarios = [
    {"usuario": "admin", "contrasena": "pass123", "tipo": "administrador"},
    {"usuario": "carlos", "contrasena": "1234e", "tipo": "empleado"}
]

# funcion para simular login
def login(usuario, contrasena):
    for user in usuarios:
        if user["usuario"] == usuario and user["contrasena"] == contrasena:
            limpiar_pantalla()
            print("Bienvenido/a, " + user['usuario'] +"")
            # --- Menu de opciones
ad            while True:
                mostrar_menuOpciones(user['tipo'])
                opcion = input("Seleccione una opción (1-4): ")

                while True:
                    if user['tipo'] == "administrador":
                        if opcion == "1":
                            limpiar_pantalla()
                            print("Registrar empleado")
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
        else:
            return True
    return False



# --- inicio del programa
respuesta = True

while  respuesta == True:
    print("\n|================= BIENVENIDO AL RESTAURANTE ""PORVENIR"" =================|")
    usuario = input("| Ingrese su nombre de usuario: ")
    contrasena = input("| Ingrese su contraseña: ")

    respuesta = login(usuario, contrasena)
    if respuesta == True:
        print("Usuario o contraseña incorrectos. Intente de nuevo.")
        continue



