from bd import Conexion


def menu_clientes(conexion):
  opcion_cliente = 0
  while opcion_cliente != "5":
    opcion_cliente = input(
        "Menú Clientes\n1- Ingresar Cliente\n2- Mostrar Clientes\n3- Editar Cliente\n4- Eliminar Cliente\n5- Volver al Menú Principal\n"
    )
    if opcion_cliente == "1":
      nombre = input("Ingrese nombre: ")
      apellido = input("Ingrese apellido: ")
      dni = input("Ingrese DNI: ")
      conexion.IngresarCliente(nombre, apellido, dni)
    elif opcion_cliente == "2":
      clientes = conexion.MostrarClientes()

      if len(clientes) > 0:
        for cliente in clientes:
          print(
              f"Nombre: {cliente[1]}, Apellido: {cliente[2]}, DNI: {cliente[3]}, ID: {cliente[0]}"
          )
      else:
        print("No hay clientes registrados.")
    elif opcion_cliente == "3":
      id_cliente = input("Ingrese ID del cliente a modificar: ")
      nombre = input("Ingrese nuevo nombre: ")
      apellido = input("Ingrese nuevo apellido: ")
      dni = input("Ingrese nuevo DNI: ")
      conexion.ModificarCliente(nombre, apellido, dni, id_cliente)
    elif opcion_cliente == "4":
      id_cliente = input("Ingrese ID del cliente a eliminar: ")
      conexion.EliminarCliente(id_cliente)
    elif opcion_cliente == "5":
      print("Volviendo al Menú Principal.")
    else:
      print("Opción no válida. Inténtalo de nuevo.")


def validarCrearVenta(id_producto, id_cliente, cantidad):
  textoDeError = ""
  if conexion.ProductoPorId(id_producto) is None:
    textoDeError += " ► No se encontró el Producto"
  if conexion.ClientePorId(id_cliente) is None:
    textoDeError += " ► No se encontró el Cliente"
  if cantidad <= 0:
    textoDeError += " ► La cantidad ingresada es menor a 0"
  return textoDeError


def menu_ventas(conexion):
  opcion_venta = 0
  while opcion_venta != "4":
    opcion_venta = input(
        "Menú Ventas\n1- Crear Venta\n2- Mostrar Ventas\n3- Mostrar Ventas por Cliente\n4- Volver al Menú Principal\n"
    )

    if opcion_venta == "1":
      id_producto = input("Ingrese ID del producto vendido: ")
      id_cliente = input("Ingrese ID del cliente: ")
      cantidad = float(
          input("Ingrese la cantidad de productos del tipo vendidos: "))

      if validarCrearVenta(id_producto, id_cliente, cantidad) == "":
        conexion.IngresarVenta(id_producto, id_cliente, cantidad)
      else:
        print(validarCrearVenta(id_producto, id_cliente, cantidad))

    elif opcion_venta == "2":
      ventas = conexion.MostrarVentas()

      if len(ventas) > 0:
        for venta in ventas:
          print(
              f"ID: {venta[0]}, ID Producto: {venta[1]}, ID Cliente: {venta[2]}, Cantidad: {venta[3]}, Precio: {venta[4]}"
          )
      else:
        print("No hay ventas registradas.")
    elif opcion_venta == "3":
      id_cliente = input("Ingrese ID del cliente para mostrar ventas: ")
      ventas = conexion.MostrarVentasPorIdCliente(id_cliente)

      if len(ventas) > 0:
        for venta in ventas:
          print(
              f"ID: {venta[0]}, ID Producto: {venta[1]}, ID Cliente: {venta[2]}, Cantidad: {venta[3]}, Precio: {venta[4]}"
          )
      else:
        print("No hay ventas registradas para este cliente.")
    elif opcion_venta == "4":
      print("Volviendo al Menú Principal.")
    else:
      print("Opción no válida. Inténtalo de nuevo.")


def menu_productos(conexion):
  opcion_producto = 0
  while opcion_producto != "4":
    opcion_producto = input(
        "Menú Productos\n1- Ingresar Producto\n2- Mostrar Productos\n3- Modificar Producto\n4- Volver al Menú Principal\n"
    )

    if opcion_producto == "1":
      nombre = input("Ingrese nombre del producto: ")
      precio = float(input("Ingrese precio del producto: "))
      conexion.IngresarProducto(nombre, precio)
    elif opcion_producto == "2":
      productos = conexion.MostrarProductos()

      if len(productos) > 0:
        for producto in productos:
          print(
              f"Nombre: {producto[1]}, Precio: {producto[2]}, ID: {producto[0]}"
          )
      else:
        print("No hay productos registrados.")
    elif opcion_producto == "3":
      id_producto = input("Ingrese ID del producto a modificar: ")
      nombre = input("Ingrese nuevo nombre: ")
      precio = float(input("Ingrese nuevo precio: "))
      conexion.ModificarProducto(nombre, precio, id_producto)
    elif opcion_producto == "4":
      print("Volviendo al Menú Principal.")
    else:
      print("Opción no válida. Inténtalo de nuevo.")


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
