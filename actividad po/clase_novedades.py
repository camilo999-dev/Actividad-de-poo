from clase_producto import Producto


class Novedades(Producto):
    def mostrar_informacion(self):
        print(f"Novedad disponible: {self.nombre}")
