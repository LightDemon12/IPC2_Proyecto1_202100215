class Piso:
    def __init__(self, nombre, R, C, F, S):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.patrones = None
        self.siguiente = None
    def __str__(self):
        return "Nombre: " + self.nombre + " R: " + self.R + " C: " + self.C + " F: " + self.F + " S: " + self.S + " Patrones: " + self.patrones + " Siguiente: " + self.siguiente
