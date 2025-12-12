class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def registrar(self):
        print(f"Usuario {self.nombre} registrado correctamente.")