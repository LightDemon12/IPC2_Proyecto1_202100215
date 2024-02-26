from piso_manager import Lista_Pisos
from xml_reader import leer_archivo_xml

def mostrar_menu():
    print("1. Mostrar lista de pisos")
    print("2. Salir")

def mostrar_pisos(lista_pisos):
    print("Pisos disponibles:")
    lista_pisos.mostrar_pisos()
    nombre_piso = input("Ingrese el nombre del piso que desea ver: ")
    lista_pisos.mostrar_matriz_piso(nombre_piso)

def main():
    # Leer archivo XML y construir la lista de pisos
    ruta_archivo_xml = 'prueba.xml'
    lista_pisos = Lista_Pisos()
    primer_piso = leer_archivo_xml(ruta_archivo_xml)
    piso_actual = primer_piso
    while piso_actual is not None:
        lista_pisos.agregar_piso(piso_actual.nombre, piso_actual.R, piso_actual.C, piso_actual.F, piso_actual.S,
                                 piso_actual.patron_actual, piso_actual.patron_nuevo)
        piso_actual = piso_actual.siguiente

    # Menú principal
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de opción que desee: ")

        if opcion == "1":
            # Mostrar lista de pisos y solicitar nombre del piso
            mostrar_pisos(lista_pisos)
        elif opcion == "2":
            # Salir del programa
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
