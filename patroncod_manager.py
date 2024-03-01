class GestorCodigosPatrones:
    def __init__(self):
        self.patron_actual = None
        self.patron_nuevo = None

    def guardar_patrones(self, patron_actual, patron_nuevo):
        self.patron_actual = patron_actual
        self.patron_nuevo = patron_nuevo

    def obtener_patron_actual(self):
        return self.patron_actual

    def obtener_patron_nuevo(self):
        return self.patron_nuevo
