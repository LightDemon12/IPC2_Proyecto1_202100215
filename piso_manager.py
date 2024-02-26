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

    def mostrar_matriz(self, patron):
        matriz = ""
        for i in range(self.R):
            for j in range(self.C):
                if patron[i * self.C + j] == 'B':
                    matriz += "B "
                else:
                    matriz += "N "
            matriz += "\n"
        return matriz

class Lista_Pisos:
    def __init__(self):
        self.head = None

    def agregar_piso(self, nombre, R, C, F, S, patron_actual, patron_nuevo):
        nuevo_piso = Nodo_Pisos(nombre, R, C, F, S, patron_actual, patron_nuevo)
        if not self.head:
            self.head = nuevo_piso
        elif nombre < self.head.nombre:
            nuevo_piso.siguiente = self.head
            self.head = nuevo_piso
        else:
            current = self.head
            while current.siguiente and nombre > current.siguiente.nombre:
                current = current.siguiente
            nuevo_piso.siguiente = current.siguiente
            current.siguiente = nuevo_piso

    def mostrar_pisos(self):
        current = self.head
        while current:
            print("Nombre:", current.nombre)
            current = current.siguiente

    def mostrar_matriz_piso(self, nombre_piso):
        current = self.head
        while current:
            if current.nombre == nombre_piso:
                print("Nombre:", current.nombre)
                print("Matriz del patrón actual:")
                print(current.mostrar_matriz(current.patron_actual))
                print("Matriz del patrón nuevo:")
                print(current.mostrar_matriz(current.patron_nuevo))
                print("-------------------------")
                return
            current = current.siguiente
        print("El piso con nombre", nombre_piso, "no fue encontrado.")
