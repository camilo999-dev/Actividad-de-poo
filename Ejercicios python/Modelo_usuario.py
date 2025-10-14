class Usuario:
    def __init__(self, nombre, apellido, cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self, sugerencia):
        print(f"{self.nombre} ha enviado la sugerencia: {sugerencia}")

    def leer(self, articulo):
        print(f"{self.nombre} está leyendo el artículo: {articulo}")

    def comprar(self, producto):
        print(f"{self.nombre} ha comprado el producto: {producto}")

    def vender(self, producto):
        print(f"{self.nombre} ha vendido el producto: {producto}")

    def realizar_reclamacion(self, detalle):
        print(f"{self.nombre} ha realizado una reclamación: {detalle}")