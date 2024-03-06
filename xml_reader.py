import xml.etree.ElementTree as ET
from os import system, startfile
from graphviz import Digraph


class Nodo_Patron:
    def __init__(self, codigo, patron):
        self.codigo = codigo
        self.patron = patron
        self.siguiente = None

class Nodo_Piso:
    def __init__(self, nombre, R, C, F, S):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F  # Agregado para almacenar el valor de F
        self.S = S  # Agregado para almacenar el valor de S
        self.patrones_head = None
        self.siguiente = None
    
    def mostrar_matrices_piso(self):
        current_patron = self.patrones_head
        while current_patron:
            print("Patron con codigo:", current_patron.codigo)
            current_patron_text = current_patron.patron
            index = 0

            for _ in range(self.R):
                new_row = ""
                for _ in range(self.C):
                    if index < len(current_patron_text):
                        new_row += current_patron_text[index] + " "
                        index += 1
                    else:
                        new_row += "- "
                print(new_row)
            print("")
            current_patron = current_patron.siguiente

class Lista_Pisos:
    def __init__(self):
        self.head = None
    
    def agregar_piso(self, nombre, R, C, F, S):
        nuevo_piso = Nodo_Piso(nombre, R, C, F, S)

        if not self.head or self.head.nombre > nombre:
            nuevo_piso.siguiente = self.head
            self.head = nuevo_piso
            return nuevo_piso

        current = self.head

        while current.siguiente and current.siguiente.nombre <= nombre:
            current = current.siguiente

        nuevo_piso.siguiente = current.siguiente
        current.siguiente = nuevo_piso

        return nuevo_piso
    
    def obtener_piso(self, nombre_piso):
        current = self.head
        while current:
            if current.nombre == nombre_piso:
                return current
            current = current.siguiente
        return None
    
    def agregar_patron(self, piso, codigo, patron):
        nuevo_patron = Nodo_Patron(codigo, patron)

        if not piso.patrones_head or piso.patrones_head.codigo > codigo:
            nuevo_patron.siguiente = piso.patrones_head
            piso.patrones_head = nuevo_patron
            return

        current = piso.patrones_head

        while current.siguiente and current.siguiente.codigo <= codigo:
            current = current.siguiente

        nuevo_patron.siguiente = current.siguiente
        current.siguiente = nuevo_patron

    def mostrar_pisos(self):
        current = self.head
        while current:
            print("Nombre:", current.nombre)
            current = current.siguiente

    def mostrar_matriz(self, piso):
        if not piso.patrones_head:
            return
        construir_matriz_nuevo(piso)
        print()

def construir_matriz_nuevo(piso, codigo_patron=None):
    current_patron = piso.patrones_head
    while current_patron:
        if codigo_patron and current_patron.codigo != codigo_patron:
            current_patron = current_patron.siguiente
            continue

        print("Patron:", current_patron.codigo)
        current_patron_text = current_patron.patron  # Corregir acceso al atributo
        index = 0

        for _ in range(piso.R):
            new_row = ""
            for _ in range(piso.C):
                if index < len(current_patron_text):
                    new_row += current_patron_text[index] + " "
                    index += 1
                else:
                    new_row += "- "
            print(new_row)
        print("")

        if codigo_patron:
            break

        current_patron = current_patron.siguiente

def leer_archivo_xml(ruta_archivo):
    lista_pisos = Lista_Pisos()
    tree = ET.parse(ruta_archivo)
    root = tree.getroot()
    for piso_elem in root.findall('piso'):
        nombre = piso_elem.get('nombre')
        R = int(piso_elem.find('R').text)
        C = int(piso_elem.find('C').text)
        F = int(piso_elem.find('F').text)  # Leer el valor de F
        S = int(piso_elem.find('S').text)  # Leer el valor de S

        nuevo_piso = lista_pisos.agregar_piso(nombre, R, C, F, S)

        patrones_elem = piso_elem.find('patrones')
        for patron_elem in patrones_elem.findall('patron'):
            codigo = patron_elem.get('codigo')
            patron = patron_elem.text
            lista_pisos.agregar_patron(nuevo_piso, codigo, patron)
    return lista_pisos




