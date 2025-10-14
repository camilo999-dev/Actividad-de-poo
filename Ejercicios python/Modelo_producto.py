class Producto:
    def __init__(self, titulo, codigo, descripcion, precio, stock=0):
        self.titulo = titulo
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = float(precio)
        self.stock = int(stock)

    def mostrar_informacion(self):
        print(f"Producto {self.codigo} | {self.titulo} | ${self.precio} | Stock: {self.stock}")
