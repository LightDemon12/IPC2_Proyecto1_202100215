import xml.etree.ElementTree as ET

class Nodo_Patron:
    def __init__(self, codigo, letra):
        self.codigo = codigo
        self.letra = letra
        self.siguiente = None
        self.anterior = None

class Nodo_Piso:
    def __init__(self, nombre, R, C, F, S):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.patrones_head_actual = None  # Inicializar patrones_head_actual
        self.patrones_head_nuevo = None    # Inicializar patrones_head_nuevo
        self.siguiente = None
        self.anterior = None

class Lista_Pisos:
    def __init__(self):
        self.head = None

    def agregar_piso(self, nombre, R, C, F, S):
        nuevo_piso = Nodo_Piso(nombre, R, C, F, S)
        if not self.head:
            self.head = nuevo_piso
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = nuevo_piso
            nuevo_piso.anterior = current
        return nuevo_piso

    def agregar_letra(self, piso, codigo, letra):
        nuevo_patron = Nodo_Patron(codigo, letra)
        if codigo[-1] == '1':
            if not piso.patrones_head_actual:
                piso.patrones_head_actual = nuevo_patron
            else:
                current = piso.patrones_head_actual
                while current.siguiente:
                    current = current.siguiente
                current.siguiente = nuevo_patron
                nuevo_patron.anterior = current
        elif codigo[-1] == '2':
            if not piso.patrones_head_nuevo:
                piso.patrones_head_nuevo = nuevo_patron
            else:
                current = piso.patrones_head_nuevo
                while current.siguiente:
                    current = current.siguiente
                current.siguiente = nuevo_patron
                nuevo_patron.anterior = current

    def mostrar_pisos(self):
        current = self.head
        while current:
            print("Nombre:", current.nombre)
            print("R:", current.R)
            print("C:", current.C)
            print("F:", current.F)
            print("S:", current.S)
            print("Patrones:")
            self.mostrar_patrones(current)
            print("-------------------------")
            current = current.siguiente

    def mostrar_patrones(self, piso):
        if piso.patrones_head_actual:
            print("Patron actual:")
            current = piso.patrones_head_actual
            while current:
                print(f"cod asociado {current.codigo} {current.letra}")
                current = current.siguiente

        if piso.patrones_head_nuevo:
            print("Patron nuevo:")
            current = piso.patrones_head_nuevo
            while current:
                print(f"cod asociado {current.codigo} {current.letra}")
                current = current.siguiente

    def ordenar_pisos_alfabeticamente(self):
        if not self.head:
            return

        sorted_head = None
        current = self.head
        while current:
            next_node = current.siguiente
            sorted_head = self.insert_sorted(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def insert_sorted(self, sorted_head, new_node):
        if not sorted_head or sorted_head.nombre >= new_node.nombre:
            new_node.siguiente = sorted_head
            if sorted_head:
                sorted_head.anterior = new_node
            return new_node

        current = sorted_head
        while current.siguiente and current.siguiente.nombre < new_node.nombre:
            current = current.siguiente

        new_node.siguiente = current.siguiente
        if current.siguiente:
            current.siguiente.anterior = new_node
        current.siguiente = new_node
        new_node.anterior = current

        return sorted_head
    
def leer_archivo_xml(ruta_archivo):
    lista_pisos = Lista_Pisos()

    tree = ET.parse(ruta_archivo)
    root = tree.getroot()

    for piso_elem in root.findall('piso'):
        nombre = piso_elem.get('nombre')
        R = int(piso_elem.find('R').text)
        C = int(piso_elem.find('C').text)
        F = int(piso_elem.find('F').text)
        S = int(piso_elem.find('S').text)

        nuevo_piso = lista_pisos.agregar_piso(nombre, R, C, F, S)

        patrones_elem = piso_elem.find('patrones')
        for patron_elem in patrones_elem.findall('patron'):
            codigo = patron_elem.get('codigo')
            patron = patron_elem.text
            for letra in patron:
                lista_pisos.agregar_letra(nuevo_piso, codigo, letra)

    return lista_pisos

def construir_matrices(lista_pisos):
    current = lista_pisos.head
    while current:
        construir_matriz_piso(current)
        current = current.siguiente

def construir_matriz_piso(piso):
    print("Nombre:", piso.nombre)
    print("R:", piso.R)
    print("C:", piso.C)
    print("Matriz:")
    print("Actual:")
    construir_matriz_actual(piso)
    print("Nuevo:")
    construir_matriz_nuevo(piso)
    print("-------------------------")

def construir_matriz_actual(piso):
    actual_letra = piso.patrones_head_actual

    for _ in range(piso.R):
        actual_row = ""
        for _ in range(piso.C):
            if actual_letra:
                actual_row += actual_letra.letra + " "
                actual_letra = actual_letra.siguiente
            else:
                actual_row += "- "
        print(actual_row)

def construir_matriz_nuevo(piso):
    nuevo_letra = piso.patrones_head_nuevo

    for _ in range(piso.R):
        nuevo_row = ""
        for _ in range(piso.C):
            if nuevo_letra:
                nuevo_row += nuevo_letra.letra + " "
                nuevo_letra = nuevo_letra.siguiente
            else:
                nuevo_row += "- "
        print(nuevo_row)

ruta_archivo_xml = 'prueba.xml'
lista_pisos = leer_archivo_xml(ruta_archivo_xml)
lista_pisos.ordenar_pisos_alfabeticamente()
lista_pisos.mostrar_pisos()
construir_matrices(lista_pisos)
