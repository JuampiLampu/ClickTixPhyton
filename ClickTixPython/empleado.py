class Empleado:
    def __init__(self):
        pass
    
    def retirar_tickets(self):
        while True:
            print("Retirar Tickets")
            print("1. Escanear QR")
            print("2. Ingresar Código Manualmente")
            print("3. Volver al menú anterior")
    
            opcion = input("Seleccione una opción: ")
    
            if opcion == "1" or opcion == "2":
                print("Imprimiendo ticket...")
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
    
    def vender_entradas(self):
        while True:
            print("Vender Entradas")
            pelicula = input("Ingrese el nombre de la película: ")
            print(f"Seleccione un horario para '{pelicula}':")
            print("1. 15:00 3D")
            print("2. 18:00 4D")
            print("3. 21:00 2D")
            print("4. Volver al menú anterior")
            opcion = input("Seleccione una opción de horario: ")
    
            if opcion == "1":
                print("Seleccionando asientos...")
                print("Imprimiendo tickets...")
                break
            elif opcion == "2":
                print("Seleccionando asientos...")
                print("Imprimiendo tickets...")
                break
            elif opcion == "3":
                print("Seleccionando asientos...")
                print("Imprimiendo tickets...")
                break
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
    
    def menu_empleado(self):
        while True:
            print("Menu del Empleado")
            print("1. Retirar Tickets")
            print("2. Vender Entradas")
            print("3. Salir")
    
            opcion = input("Seleccione una opción: ")
    
            if opcion == "1":
                self.retirar_tickets()
            elif opcion == "2":
                self.vender_entradas()
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
