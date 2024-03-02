import xml.etree.ElementTree as ET

class NodoPatron:
    def __init__(self, codigo, patron):
        self.codigo = codigo
        self.patron = patron
        self.siguiente = None

class NodoPiso:
    def __init__(self, nombre, R, C, F, S):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.patrones_head = None
        self.siguiente = None

class ListaPisos:
    def __init__(self):
        self.head = None

    def agregar_piso(self, nombre, R, C, F, S):
        nuevo_piso = NodoPiso(nombre, R, C, F, S)
        if not self.head:
            self.head = nuevo_piso
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = nuevo_piso

    def obtener_piso(self, nombre_piso):
        current = self.head
        while current:
            if current.nombre == nombre_piso:
                return current
            current = current.siguiente
        return None
    
def buscar_piso_y_patrones(ruta_archivo, nombre_piso, codigo_patron_actual, codigo_patron_nuevo):
    try:
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()

        for piso_elem in root.findall('piso'):
            nombre = piso_elem.get('nombre')
            if nombre == nombre_piso:
                R = int(piso_elem.find('R').text)
                C = int(piso_elem.find('C').text)
                F = int(piso_elem.find('F').text)
                S = int(piso_elem.find('S').text)

                nuevo_piso = NodoPiso(nombre, R, C, F, S)
                patrones_elem = piso_elem.find('patrones')
                for patron_elem in patrones_elem.findall('patron'):
                    codigo = patron_elem.get('codigo')
                    patron = patron_elem.text
                    if codigo == codigo_patron_actual or codigo == codigo_patron_nuevo:
                        if not nuevo_piso.patrones_head:
                            nuevo_piso.patrones_head = NodoPatron(codigo, patron)
                        else:
                            current = nuevo_piso.patrones_head
                            while current.siguiente:
                                current = current.siguiente
                            current.siguiente = NodoPatron(codigo, patron)
                return nuevo_piso

        return None

    except Exception as e:
        print(f"Error al procesar el archivo XML: {e}")
        return None


    except Exception as e:
        print(f"Error al procesar el archivo XML: {e}")
        return None

def mostrar_datos_piso(piso):
    if piso:
        print("Piso encontrado:")
        print(f"Nombre: {piso.nombre}")
        print(f"R: {piso.R}")
        print(f"C: {piso.C}")
        print(f"F: {piso.F}")
        print(f"S: {piso.S}")
        print("Patrones:")
        current = piso.patrones_head
        while current:
            print(f"Código: {current.codigo}, Patrón: {current.patron}")
            current = current.siguiente
    else:
        print("No se encontró el piso o los códigos de patrón especificados.")

class PatronCodManager:
    def __init__(self):
        self.nombre_piso = None
        self.codigo_patron_actual = None
        self.codigo_patron_nuevo = None
        self.R = None
        self.C = None
        self.F = None
        self.S = None

    def solicitar_codigos_patron(self, nombre_piso, R, C, F, S):
        self.nombre_piso = nombre_piso
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.codigo_patron_actual = input("Ingrese el código del patrón actual: ")
        self.codigo_patron_nuevo = input("Ingrese el código del nuevo patrón: ")

    def mostrar_datos(self):
        print("Datos guardados en PatronCodManager:")
        print(f"Nombre del piso: {self.nombre_piso}")
        print(f"R: {self.R}")
        print(f"C: {self.C}")
        print(f"F: {self.F}")
        print(f"S: {self.S}")
        print(f"Código del patrón actual: {self.codigo_patron_actual}")
        print(f"Código del nuevo patrón: {self.codigo_patron_nuevo}")

    def realizar_operaciones(self):
        # Realizar operaciones con los datos guardados
        pass





