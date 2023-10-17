import sqlite3


class Conexion:

  def __init__(self, nombreBD):
    self.conexion = sqlite3.connect(nombreBD)
    self.cursor = self.conexion.cursor()

  def CrearCliente(self):
    self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS CLIENTE(
          id INTEGER PRIMARY KEY,
          nombre TEXT,
          apellido TEXT,
          dni TEXT
        )
        ''')
    self.conexion.commit()

  def ProductoPorId(self, id):
    self.cursor.execute("SELECT * FROM PRODUCTO WHERE id = ?", (id, ))
    
    producto = self.cursor.fetchone() 
    return producto
    
  def ClientePorId(self, id):
    self.cursor.execute("SELECT * FROM CLIENTE WHERE id = ?", (id, ))

    cliente = self.cursor.fetchone() 
    return cliente

  def CrearProducto(self):
    self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUCTO(
          id INTEGER PRIMARY KEY,
          nombre TEXT,
          precio DOUB
        )
        ''')
    self.conexion.commit()

  def CrearVenta(self):
    self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS VENTA(
          id INTEGER PRIMARY KEY,
          id_producto INTEGER,
          id_cliente INTEGER,
          cantidad INTEGER,
          precio DOUBLE,
          FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id),
          FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id)
        )
        ''')

    self.conexion.commit()

  def MostrarVentas(self):
    self.cursor.execute("SELECT * FROM VENTA")
    ventas = self.cursor.fetchall()
    return ventas

  def MostrarVentasPorIdCliente(self, idCliente):
    self.cursor.execute("SELECT * FROM VENTA WHERE id_cliente = ?", idCliente)
    ventas = self.cursor.fetchall()
    return ventas

  def IngresarVenta(self, idProducto, idCliente, cantidad):
    producto = self.ProductoPorId(idProducto)
    precio = producto[2]
    print(precio)
    precioNuevo = precio * cantidad
    print(precioNuevo)
    self.cursor.execute(
        "INSERT INTO VENTA (id_producto,id_cliente,cantidad,precio) VALUES (?,?,?,?)",
        (idProducto, idCliente, cantidad, precioNuevo))
    self.conexion.commit()

  def IngresarCliente(self, nombre, apellido, dni):
    self.cursor.execute(
        "INSERT INTO CLIENTE (nombre,apellido,dni) VALUES (?,?,?)",
        (nombre, apellido, dni))
    self.conexion.commit()

  def MostrarClientes(self):
    self.cursor.execute("SELECT * FROM CLIENTE")
    clientes = self.cursor.fetchall()
    return clientes

  def ModificarCliente(self, nombre, apellido, dni, id):
    self.cursor.execute(
        "UPDATE CLIENTE SET nombre=?,apellido=?,dni=? WHERE id = ?",
        (nombre, apellido, dni, id))
    self.conexion.commit()

  def EliminarCliente(self, id):
    self.cursor.execute("DELETE FROM CLIENTE WHERE id = ?", (id, ))
    self.conexion.commit()
    

  def IngresarProducto(self, nombre, precio):
    self.cursor.execute("INSERT INTO PRODUCTO (nombre,precio) VALUES (?,?)",
                        (nombre, precio))
    self.conexion.commit()

  def MostrarProductos(self):
    self.cursor.execute("SELECT * FROM PRODUCTO")
    productos = self.cursor.fetchall()
    return productos

  def ModificarProducto(self, nombre, precio, id):
    self.cursor.execute("UPDATE PRODUCTO SET nombre=?,precio=? WHERE id = ?",
                        (nombre, precio, id))
    self.conexion.commit()

  def EliminarProducto(self, id):
    self.cursor.execute("DELETE FROM PRODUCTO WHERE id = ?", (id, ))
    self.conexion.commit()


  def CerrarBD(self):
    self.cursor.close()
    self.conexion.close()
    
tiago = 10
