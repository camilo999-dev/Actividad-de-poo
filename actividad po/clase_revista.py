from clase_producto import Producto


class Revista(Producto):
    def mostrar_informacion(self):
        print(f"Revista: {self.nombre} publicada el día de hoy.")
