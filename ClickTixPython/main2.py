from Login import Login
from Admin import Admin
from Empleado import Empleado

bucle = 0

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