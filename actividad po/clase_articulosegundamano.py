from clase_producto import Producto


class ArticuloSegundaMano(Producto):
    def mostrar_informacion(self):
        print(f"Artículo de Segunda Mano: {self.nombre}, estado aceptable.")
        