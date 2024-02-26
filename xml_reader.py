import xml.etree.ElementTree as ET
from piso_manager import Nodo_Pisos

def leer_archivo_xml(ruta_archivo):
    primer_piso = None
    ultimo_piso = None

    tree = ET.parse(ruta_archivo)
    root = tree.getroot()

    for piso_elem in root.findall('piso'):
        nombre = piso_elem.get('nombre')
        R = int(piso_elem.find('R').text)  # Convertir a entero
        C = int(piso_elem.find('C').text)  # Convertir a entero
        F = int(piso_elem.find('F').text)  # Convertir a entero
        S = int(piso_elem.find('S').text)  # Convertir a entero

        patrones = piso_elem.find('patrones')
        patron_actual = patrones[0].text  # Primer patron
        patron_nuevo = patrones[1].text   # Segundo patron

        nodo_piso = Nodo_Pisos(nombre, R, C, F, S, patron_actual, patron_nuevo)

        if primer_piso is None:
            primer_piso = nodo_piso
            ultimo_piso = nodo_piso
        else:
            ultimo_piso.siguiente = nodo_piso
            ultimo_piso = nodo_piso

    return primer_piso
