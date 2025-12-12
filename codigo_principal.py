

class Servidor:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.clientes_conectados = []

    def conectar_cliente(self, cliente):
        print(f"Cliente {cliente} conectado al servidor {self.nombre}.")


class Procesador:
    def procesar(self, solicitud):
        print(f"Procesando solicitud: {solicitud}")


class Recolector:
    def __init__(self, id_recolector):
        self.id_recolector = id_recolector

    def envia_novedades(self, novedades):
        print(f"Recolector {self.id_recolector} envía novedades: {', '.join(novedades)}")


class Indexador:
    def indexar(self, contenido):
        print(f"Indexando contenido: {contenido}")


class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def registrar(self):
        print(f"Usuario {self.nombre} registrado correctamente.")


class Producto:
    def __init__(self, nombre, codigo, descripcion, precio, editorial):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.editorial = editorial

    def mostrar_informacion(self):
        print("=== Información del Producto ===")
        print(f"Nombre: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Precio: {self.precio}")
        print(f"Editorial: {self.editorial}")
        print("================================")


class Editorial:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def publicar(self, producto):
        print(f"Editorial {self.nombre} publica: {producto.nombre}")


class Hilo:
    def __init__(self, nombre, tema):
        self.nombre = nombre
        self.tema = tema
        self.mensajes = []

    def agregar_mensaje(self, usuario, mensaje):
        print(f"{usuario} escribió en el hilo '{self.nombre}': {mensaje}")


# ===== Subclases de Producto =====

class Libro(Producto):
    def mostrar_informacion(self):
        print(f"Libro: {self.nombre} mostrado correctamente.")


class Revista(Producto):
    def mostrar_informacion(self):
        print(f"Revista: {self.nombre} publicada el día de hoy.")


class ArticuloSegundaMano(Producto):
    def mostrar_informacion(self):
        print(f"Artículo de Segunda Mano: {self.nombre}, estado aceptable.")


class Novedades(Producto):
    def mostrar_informacion(self):
        print(f"Novedad disponible: {self.nombre}")


class ArticuloOnline(Producto):
    def mostrar_informacion(self):
        print(f"Artículo Online disponible: {self.nombre}")


# ==========================================
# DEMOSTRACIÓN: IMPRIMIR MENSAJE DE CADA CLASE
# ==========================================

servidor = Servidor("Servidor Central", "192.168.1.1")
servidor.conectar_cliente("Cliente01")

procesador = Procesador()
procesador.procesar("Solicitud de ejemplo")

recolector = Recolector("RC-001")
recolector.envia_novedades(["Nuevo libro", "Nueva revista"])

indexador = Indexador()
indexador.indexar("Contenido importante")

usuario = Usuario("Carlos", "carlos@mail.com")
usuario.registrar()

editorial = Editorial("Planeta", "Colombia")
producto = Producto("Producto Base", "P001", "Descripción base", 15000, "Planeta")
producto.mostrar_informacion()

editorial.publicar(producto)

hilo = Hilo("Debate General", "Literatura")
hilo.agregar_mensaje("Carlos", "Me encanta este libro.")

# Subclases
libro = Libro("El Quijote", "L001", "Novela clásica", 30000, "Planeta")
libro.mostrar_informacion()

revista = Revista("Semana", "R001", "Actualidad", 10000, "Publicaciones SA")
revista.mostrar_informacion()

art2 = ArticuloSegundaMano("Libro Usado", "A002", "Usado pero bueno", 5000, "Planeta")
art2.mostrar_informacion()

novedad = Novedades("Novedad Literaria", "N001", "Nuevo lanzamiento", 25000, "Planeta")
novedad.mostrar_informacion()

online = ArticuloOnline("Ebook Python", "O001", "Libro digital", 20000, "DigitalHouse")
online.mostrar_informacion()