from clase_producto import Producto


class ArticuloOnline(Producto):
    def mostrar_informacion(self):
        print(f"Artículo Online disponible: {self.nombre}")