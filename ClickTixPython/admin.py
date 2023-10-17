class Admin:
    def __init__(self):
        pass
    
    
    def gestionar_abm(self):
        while True:
            print("Gestionar ABM")
            print("1. ABM Pelicula")
            print("2. ABM Funciones")
            print("3. ABM Empleados")
            print("4. ABM Promociones")
            print("5. ABM Categorias")
            print("6. Volver al menú anterior")
    
            opcion = input("Seleccione una opción: ")
    
            if opcion == "1":
                print("Realizando ABM Pelicula...")
            elif opcion == "2":
                print("Realizando ABM Funciones...")
            elif opcion == "3":
                print("Realizando ABM Empleados...")
            elif opcion == "4":
                print("Realizando ABM Promociones...")
            elif opcion == "5":
                print("Realizando ABM Categorias...")
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
  
    def generar_reportes(self):
        while True:
            print("Generar Reportes")
            print("1. Por Semana")
            print("2. Por Mes")
            print("3. Por Año")
            print("4. Por Película")
            print("5. Por Sucursal")
            print("6. Volver al menú anterior")
    
            opcion = input("Seleccione una opción: ")
    
            if opcion == "1":
                print("Generando reporte por semana...")
            elif opcion == "2":
                print("Generando reporte por mes...")
            elif opcion == "3":
                print("Generando reporte por año...")
            elif opcion == "4":
                print("Generando reporte por película...")
                pelicula = input("Ingrese el nombre de la película: ")
                submenu_opcion = input("Seleccione una opción para la película (1. Semana, 2. Mes, 3. Año): ")
                if submenu_opcion == "1":
                    print("Generando informe por semana para la película", pelicula)
                elif submenu_opcion == "2":
                    print("Generando informe por mes para la película", pelicula)
                elif submenu_opcion == "3":
                    print("Generando informe por año para la película", pelicula)
                else:
                    print("Opción no válida. Por favor, elija una opción válida para la película.")
            elif opcion == "5":
                print("Generando reporte por sucursal...")
                sucursal = input("Ingrese el nombre de la sucursal: ")
                submenu_opcion = input("Seleccione una opción para la sucursal (1. Semana, 2. Mes, 3. Año): ")
                if submenu_opcion == "1":
                    print("Generando informe por semana para la sucursal", sucursal)
                elif submenu_opcion == "2":
                    print("Generando informe por mes para la sucursal", sucursal)
                elif submenu_opcion == "3":
                    print("Generando informe por año para la sucursal", sucursal)
                else:
                    print("Opción no válida. Por favor, elija una opción válida para la sucursal.")
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
    def menu_admin(self):
        while True:
            print("Menu del Administrador")
            print("1. Gestionar ABM")
            print("2. Generar Reportes")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestionar_abm()
            elif opcion == "2":
                self.generar_reportes()
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
