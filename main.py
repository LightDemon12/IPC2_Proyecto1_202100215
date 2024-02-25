from piso_manager import Lista_Pisos
from xml_reader import leer_archivo_xml


def main():
    # Lector XML
    ruta_archivo_xml = 'prueba.xml'
    primer_piso = leer_archivo_xml(ruta_archivo_xml)

    # Lista de pisos
    lista_pisos = Lista_Pisos()
    piso_actual = primer_piso
    while piso_actual is not None:
        lista_pisos.agregar_piso(piso_actual.nombre, piso_actual.R, piso_actual.C, piso_actual.F, piso_actual.S,
                                 piso_actual.patron_actual, piso_actual.patron_nuevo)
        piso_actual = piso_actual.siguiente

    # Mostrar pisos
    print("Pisos disponibles:")
    lista_pisos.mostrar_pisos()

   

if __name__ == "__main__":
    main()
