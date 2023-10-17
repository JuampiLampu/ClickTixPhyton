class Login:

    def __init__(self):
        pass  

    def iniciarSesion(self):
        usuario = input("Ingrese su nombre de usuario: ")
        passw = input("Ingrese su contraseña: ")

        if usuario == "admin" and passw == "admin":
            return 1
        elif usuario == "emp" and passw == "emp":
            return 2
        else:
            return -1