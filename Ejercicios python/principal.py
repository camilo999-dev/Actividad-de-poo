# ======================================
#        SISTEMA DE PUBLICACIONES
# ======================================
#        Autor: Camilo Atuesta
# ======================================


# ======================================
#            CLASE EDITORIAL
# ======================================
class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.publicaciones = []

    def publicar(self, producto):
        self.publicaciones.append(producto)
        print(f"La editorial '{self.nombre}' ha publicado el producto: {producto}")

    def enviar_informacion(self):
        print(f"\n=== Información de la Editorial ===")
        print(f"Nombre: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        if self.publicaciones:
            print(f"Publicaciones: {', '.join(self.publicaciones)}")
        else:
            print("Publicaciones: Ninguna")
        print("===================================")



# ======================================
#            CLASE SERVIDOR
# ======================================
class Servidor:
    def __init__(self, nombre_servidor):
        self.nombre_servidor = nombre_servidor
        self.datos_compra = []
        self.datos_venta = []

    def muestra_pagina(self, pagina):
        print(f"Mostrando la página: {pagina} desde el servidor {self.nombre_servidor}")

    def envia_sugerencia(self, sugerencia):
        print(f"Enviando sugerencia al servidor {self.nombre_servidor}: {sugerencia}")

    def envia_datos_de_compra(self, datos):
        self.datos_compra.append(datos)
        print(f"Datos de compra enviados al servidor {self.nombre_servidor}: {datos}")

    def envia_datos_de_venta(self, datos):
        self.datos_venta.append(datos)
        print(f"Datos de venta enviados al servidor {self.nombre_servidor}: {datos}")



# ======================================
#            CLASE PROCESADOR
# ======================================
class Procesador:
    def __init__(self, id_procesador, editorial):
        self.id_procesador = id_procesador
        self.catalogo = []
        self.stock = {}
        self.editorial = editorial

    def mandar_datos_de_venta(self, datos_venta):
        print(f"Procesador {self.id_procesador} envía datos de venta: {datos_venta}")

    def mandar_articulo_online(self, articulo):
        print(f"Procesador {self.id_procesador} publica artículo online: {articulo}")

    def envia_sugerencia_administrador(self, sugerencia):
        print(f"Sugerencia enviada al administrador desde procesador {self.id_procesador}: {sugerencia}")

    def modificar_stock(self, producto, cantidad):
        self.stock[producto] = cantidad
        print(f"Stock actualizado para {producto}: {cantidad} unidades")

    def realizar_cobro(self, usuario, monto):
        print(f"Cobro de ${monto} realizado al usuario {usuario}")

    def realizar_pago(self, proveedor, monto):
        print(f"Pago de ${monto} realizado al proveedor {proveedor}")

    def actualiza_catalogo(self, producto):
        if producto not in self.catalogo:
            self.catalogo.append(producto)
            print(f"Producto '{producto}' agregado al catálogo de la editorial '{self.editorial.nombre}'.")
        else:
            print(f"Producto '{producto}' ya está en el catálogo de la editorial '{self.editorial.nombre}'.")

    def realiza_busqueda(self, termino):
        print(f"Buscando '{termino}' en el catálogo del procesador {self.id_procesador}")
        if self.catalogo:
            primer = self.catalogo[0]
            if termino.lower() in primer.lower():
                print(f"Resultado encontrado: {primer}")
            else:
                print("No se encontró el término buscado.")
        else:
            print("El catálogo está vacío.")



# ======================================
#            CLASE RECOLECTOR
# ======================================
class Recolector:
    def __init__(self, id_recolector):
        self.id_recolector = id_recolector
        self.novedades = []

    def envia_novedades(self, novedades):
        self.novedades.extend(novedades)
        texto = ", ".join(novedades) if len(novedades) == 1 else " y ".join(novedades)
        print(f"Recolector {self.id_recolector} envía novedades: {texto}")



# ======================================
#            CLASE INDEXADOR
# ======================================
class Indexador:
    def __init__(self, id_indexador):
        self.id_indexador = id_indexador
        self.indices = {}

    def indexa(self, elemento, categoria):
        if categoria not in self.indices:
            self.indices[categoria] = []
        self.indices[categoria].append(elemento)
        print(f"Indexador {self.id_indexador} ha indexado '{elemento}' en la categoría '{categoria}'.")



# ======================================
#            CLASE USUARIO
# ======================================
class Usuario:
    def __init__(self, nombre, apellido, cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self, sugerencia):
        print(f"{self.nombre} ha enviado la sugerencia: {sugerencia}")

    def leer(self, articulo):
        print(f"{self.nombre} está leyendo el artículo: {articulo}")

    def comprar(self, producto):
        print(f"{self.nombre} ha comprado el producto: {producto}")

    def vender(self, producto):
        print(f"{self.nombre} ha vendido el producto: {producto}")

    def realizar_reclamacion(self, detalle):
        print(f"{self.nombre} ha realizado una reclamación: {detalle}")



# ======================================
#            CLASE PRODUCTO
# ======================================
class Producto:
    def __init__(self, nombre, codigo, descripcion, precio, editorial):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.editorial = editorial

    def mostrar_informacion(self):
        print("\n=== Información del Producto ===")
        print(f"Nombre: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Precio: ${self.precio}")
        print(f"Editorial: {self.editorial.nombre}")
        print("===============================")



# ======================================
#            CLASE HILO
# ======================================
class Hilo:
    def __init__(self, nombre, tema):
        self.nombre = nombre
        self.tema = tema
        self.mensajes = []

    def agregar_mensaje(self, usuario, mensaje):
        entrada = f"{usuario}: {mensaje}"
        self.mensajes.append(entrada)
        print(f"Nuevo mensaje agregado al hilo '{self.nombre}' por {usuario}.")

    def mostrar_mensajes(self):
        print(f"\n📌 Hilo: {self.nombre} | Tema: {self.tema}")
        if not self.mensajes:
            print("No hay mensajes aún.")
        else:
            print(f" - {self.mensajes[0]}")



# ======================================
#            CLASE LIBRO
# ======================================
class Libro(Producto):
    def __init__(self, nombre, codigo, descripcion, precio, editorial, autor, genero):
        super().__init__(nombre, codigo, descripcion, precio,editorial)
        self.autor = autor
        self.genero = genero
        self.paginas = 0

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print("===============================")



# ======================================
#     SUBCLASE: ARTICULO SEGUNDA MANO
# ======================================
class ArticuloSegundaMano(Producto):
    def __init__(self, nombre, codigo, descripcion, precio, editorial, estado, vendedor):
        super().__init__(nombre, codigo, descripcion, precio, editorial)
        self.estado = estado  # ejemplo: 'Bueno', 'Regular', 'Malo'
        self.vendedor = vendedor

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Estado: {self.estado}")
        print(f"Vendedor: {self.vendedor}")
        print("===============================")



# ======================================
#            SUBCLASE: NOVEDADES
# ======================================
class Novedades(Producto):
    def __init__(self, nombre, codigo, descripcion, precio, editorial, fecha_novedad):
        super().__init__(nombre, codigo, descripcion, precio, editorial)
        self.fecha_novedad = fecha_novedad  # formato libre, p. ej. "Octubre 2025"

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Fecha de Novedad: {self.fecha_novedad}")
        print("===============================")



# ======================================
#         SUBCLASE: ARTICULO ONLINE
# ======================================
class ArticuloOnline(Producto):
    def __init__(self, nombre, codigo, descripcion, precio, editorial, url, formato):
        super().__init__(nombre, codigo, descripcion,precio, editorial)
        self.url = url
        self.formato = formato  # p. ej. 'PDF', 'HTML', 'EPUB'

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"URL: {self.url}")
        print(f"Formato: {self.formato}")
        print("===============================")



# ======================================
#               SUBCLASE: EBOOK
# ======================================
class Ebook(Producto):
    def __init__(self, nombre, codigo, descripcion, precio, editorial, archivo, tamaño_mb):
        super().__init__(nombre, codigo, descripcion, precio, editorial)
        self.archivo = archivo  # nombre del archivo o identificador
        self.tamaño_mb = tamaño_mb

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Archivo: {self.archivo}")
        print(f"Tamaño (MB): {self.tamaño_mb}")
        print("===============================")



# ======================================
#            EJEMPLO DE USO
# ======================================
if __name__ == "__main__":
    # Editorial única
    editorial_unica = Editorial("Planeta", "Calle 45 #10-20", "3105559999")

    # Usuario
    usuario1 = Usuario("Camilo", "Atuesta", "C123", "Bogotá", "camiloA", "1234")

    # Libro principal
    libro1 = Libro(
        "Los mejores jugadores de cada país",
        "L001",
        "Análisis de los jugadores más destacados de cada nación.",
        52000,
        editorial_unica,
        "Rodolfo Hernández",
        "Deporte"
    )
    libro1.mostrar_informacion()
    editorial_unica.publicar(libro1.nombre)

    # Artículo de segunda mano
    art2 = ArticuloSegundaMano(
        "Balón de colección - Mundial 2014",
        "S001",
        "Balón autografiado en buen estado.",
        120000,
        editorial_unica,
        "Bueno",
        "Juan Pérez"
    )
    art2.mostrar_informacion()
    editorial_unica.publicar(art2.nombre)

    # Novedad
    nov = Novedades(
        "Guía de entrenadores 2025",
        "N001",
        "Nuevas técnicas y tácticas por país.",
        38000,
        editorial_unica,
        "Octubre 2025"
    )
    nov.mostrar_informacion()
    editorial_unica.publicar(nov.nombre)

    # Artículo online
    online = ArticuloOnline(
        "Ranking interactivo de jugadores",
        "O001",
        "Base de datos online con estadísticas por país.",
        0,
        editorial_unica,
        "https://example.com/ranking",
        "HTML"
    )
    online.mostrar_informacion()
    editorial_unica.publicar(online.nombre)

    # Ebook
    ebook = Ebook(
        "Los mejores jugadores de cada país - Edición digital",
        "E001",
        "Versión ebook con enlaces y multimedia.",
        22000,
        editorial_unica,
        "los_mejores_jugadores.epub",
        12.5
    )
    ebook.mostrar_informacion()
    editorial_unica.publicar(ebook.nombre)

    # Mostrar info de la editorial (lista las publicaciones)
    editorial_unica.enviar_informacion()

    # Hilo de discusión
    hilo1 = Hilo("Foro de Deportes", "Los mejores jugadores de cada país")
    hilo1.agregar_mensaje(usuario1.nombre, "Excelente libro, me encantaron los datos sobre Brasil y Argentina.")
    hilo1.mostrar_mensajes()

    # Procesador ejemplo (se agrega al catálogo el primer producto manualmente)
    procesador = Procesador("P01", editorial_unica)
    procesador.actualiza_catalogo(libro1.nombre)
    procesador.actualiza_catalogo(ebook.nombre)
    procesador.realiza_busqueda("jugadores")
