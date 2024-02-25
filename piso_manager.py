class Nodo_Pisos:
    def __init__(self, nombre, R, C, F, S, patron_actual, patron_nuevo):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.patron_actual = patron_actual
        self.patron_nuevo = patron_nuevo
        self.siguiente = None

class Lista_Pisos:
    def __init__(self):
        self.head = None

    def agregar_piso(self, nombre, R, C, F, S, patron_actual, patron_nuevo):
        nuevo_piso = Nodo_Pisos(nombre, R, C, F, S, patron_actual, patron_nuevo)
        if not self.head:
            self.head = nuevo_piso
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = nuevo_piso

    def mostrar_pisos(self):
        current = self.head
        while current:
            print("Nombre:", current.nombre)
            print("R:", current.R)
            print("C:", current.C)
            print("F:", current.F)
            print("S:", current.S)
            print("Patrón Actual:", current.patron_actual)
            print("Patrón Nuevo:", current.patron_nuevo)
            print("-------------------------")
            current = current.siguiente