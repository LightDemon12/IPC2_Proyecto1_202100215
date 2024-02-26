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

# Ejemplo de uso:
ruta_archivo_xml = 'prueba.xml'
lista_pisos = leer_archivo_xml(ruta_archivo_xml)
lista_pisos.mostrar_pisos()
