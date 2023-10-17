from login import Login
from admin import Admin
from empleado import Empleado
from bd import Conexion


bucle = 0


if __name__ == "__main__":
  nombreBD = "ClickTix.db"
  conexion = Conexion(nombreBD)
  conexion.CrearCliente()
  conexion.CrearProducto()
  conexion.CrearVenta()

  opcion_principal = 0
  while opcion_principal != "4":
    opcion_principal = input(
        "Menú Principal\n1- Trabajar con Clientes\n2- Trabajar con Productos\n3- Trabajar con Ventas\n4- Salir\n"
    )

    if opcion_principal == "1":
      menu_clientes(conexion)
    elif opcion_principal == "2":
      menu_productos(conexion)
    elif opcion_principal == "3":
      menu_ventas(conexion)
    elif opcion_principal == "4":
      print("Adiós.")
      conexion.CerrarBD()
    else:
      print("Opción no válida. Inténtalo de nuevo.")


      print("prueba")
      

while bucle != 1:
    print("1-Iniciar Sesion \n2-Salir")
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 1:
        login = Login()
        tipoUsuario = login.iniciarSesion()
        if tipoUsuario == 1:
            admin = Admin()
            admin.menu_admin()
        elif tipoUsuario == 2:
            empleado = Empleado()
            empleado.menu_empleado()
        else:
            print("Usuario desconocido")
    elif opcion == 2:
        bucle = 1 

print("Has salido correctamente")

