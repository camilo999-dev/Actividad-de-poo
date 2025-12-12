class Hilo:
    def __init__(self, nombre, tema):
        self.nombre = nombre
        self.tema = tema
        self.mensajes = []

    def agregar_mensaje(self, usuario, mensaje):
        print(f"{usuario} escribió en el hilo '{self.nombre}': {mensaje}")