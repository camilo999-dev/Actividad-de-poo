class Servidor:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.clientes_conectados = []

    def conectar_cliente(self, cliente):
        print(f"Cliente {cliente} conectado al servidor {self.nombre}.")