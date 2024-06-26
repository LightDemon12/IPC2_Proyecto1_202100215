from xml_reader import leer_archivo_xml
from patroncod_manager import PatronCodManager


def menu():
    print("Menu:")
    print("1. Mostrar lista de pisos")
    print("2. Mostrar matrices de un piso")
    print("3. Salir")

def main():
    while True:
        # Solicitar al usuario que ingrese la ruta del archivo XML
        ruta_archivo_xml = input("Ingrese la ruta del archivo XML: ")

        # Intentar leer el archivo XML y procesar los datos
        lista_pisos = leer_archivo_xml(ruta_archivo_xml)

        # Verificar si se pudo leer el archivo XML correctamente
        if lista_pisos:
            # Si se pudo leer correctamente, continuar con el resto del programa
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
                        patron_manager.solicitar_codigos_patron(nombre_piso, R, C, F, S, ruta_archivo_xml)
                        patron_manager.mostrar_datos()
                        patron_manager.realizar_operaciones()
                        # Obtener los patrones actuales y nuevos como cadenas de texto
                        patron_actual = patron_manager.patron_actual.patron
                        patron_nuevo = patron_manager.patron_nuevo.patron
                        print("Llamando a la función calcular_costo_minimo...")
                        # Llamar a la función calcular_costo_minimo con los patrones como cadenas de texto
                        costo_minimo = patron_manager.calcular_costo_minimo()
                        print("Se ha calculado el costo mínimo.")
                        print("Costo mínimo:", costo_minimo)
                    else:
                        print("No se encontró el piso con el nombre especificado.")
                elif opcion == '3':
                    print("Saliendo del programa...")
                    return
                else:
                    print("Opción no válida. Por favor, ingrese un número válido.")
        else:
            # Si no se pudo leer correctamente, pedir al usuario que vuelva a ingresar la ruta del archivo
            print("No se pudo leer el archivo XML. Por favor, verifique la ruta e inténtelo de nuevo.")

if __name__ == "__main__":
    main()
