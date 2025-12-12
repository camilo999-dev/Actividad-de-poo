class Recolector:
    def __init__(self, id_recolector):
        self.id_recolector = id_recolector

    def envia_novedades(self, novedades):
        print(f"Recolector {self.id_recolector} envía novedades: {', '.join(novedades)}")
