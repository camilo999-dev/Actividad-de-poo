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