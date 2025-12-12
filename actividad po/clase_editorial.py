class Editorial:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def publicar(self, producto):
        print(f"Editorial {self.nombre} publica: {producto.nombre}")