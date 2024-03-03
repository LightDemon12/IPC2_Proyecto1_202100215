from xml_reader import leer_archivo_xml
from patroncod_manager import PatronCodManager
from patroncod_manager import calcular_costo_minimo

def menu():
    print("Menu:")
    print("1. Mostrar lista de pisos")
    print("2. Mostrar matrices de un piso")
    print("3. Salir")

def main():
    ruta_archivo_xml = 'prueba.xml'
    lista_pisos = leer_archivo_xml(ruta_archivo_xml)
    patron_manager = PatronCodManager()

    while True:
        menu()
        opcion = input("Ingrese el número de opción: ")

        if opcion == '1':
            lista_pisos.mostrar_pisos()
        elif opcion == '2':
            nombre_piso = input("Ingrese el nombre del piso: ")
            piso = lista_pisos.obtener_piso(nombre_piso)
            if piso:
                piso.mostrar_matrices_piso()
                R = piso.R
                C = piso.C
                F = piso.F
                S = piso.S
                patron_manager.solicitar_codigos_patron(nombre_piso, R, C, F, S)  # Solicitar códigos de patrón al usuario
                patron_manager.mostrar_datos()  # Mostrar los datos ingresados por el usuario
                patron_manager.realizar_operaciones()  # Realizar operaciones con los códigos de patrón
                # Llamar a la función calcular_costo_minimo
                costo_minimo = calcular_costo_minimo(patron_manager.patron_actual, patron_manager.patron_nuevo, F, S)
                print("Costo mínimo:", costo_minimo)
            else:
                print("No se encontró el piso con el nombre especificado.")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
