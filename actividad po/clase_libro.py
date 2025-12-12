from clase_producto import Producto

class Libro(Producto):
    def mostrar_informacion(self):
        print(f"Libro: {self.nombre} mostrado correctamente.")