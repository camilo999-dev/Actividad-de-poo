class Cliente:
    def __init__(self, nombre, apellido, documento, direccion, correo):
        super().__init__(nombre, apellido, documento)
        self.direccion = direccion
        self.correo = correo
        self.historial_compras = []

    def agregar_compra_al_historial(self, venta):
        self.historial_compras.append(venta)
        print(f"[HISTORIAL] {self.nombre_completo()} agregó la venta id={venta.id_venta} al historial.")
