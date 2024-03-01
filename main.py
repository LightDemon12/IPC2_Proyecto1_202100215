from xml_reader import leer_archivo_xml
from patroncod_manager import GestorCodigosPatrones  

def mostrar_lista_pisos(lista_pisos):
    print("Lista de pisos:")
    lista_pisos.mostrar_pisos()

def mostrar_matrices_piso(lista_pisos, gestor_patrones):  
    nombre_piso = input("Ingrese el nombre del piso: ")
    piso = lista_pisos.obtener_piso(nombre_piso)
    
    if piso:
        print("Nombre:", piso.nombre)
        piso.mostrar_matrices_piso()  # Muestra todas las matrices del piso
        
        # El usuario elige los patrones actual y nuevo
        patron_actual = input("Ingrese el código del patrón actual: ")
        patron_nuevo = input("Ingrese el código del nuevo patrón deseado: ")
        
        # Guardar los patrones en el gestor
        gestor_patrones.guardar_patrones(patron_actual, patron_nuevo)
    else:
        print("No se encontró el piso con el nombre especificado.")
        
def mostrar_patrones(gestor_patrones, lista_pisos):
    patron_actual = gestor_patrones.obtener_patron_actual()
    patron_nuevo = gestor_patrones.obtener_patron_nuevo()

    if patron_actual and patron_nuevo:
        print("Patrón actual:")
        mostrar_matriz_piso(lista_pisos, patron_actual)
        print("\nPatrón nuevo:")
        mostrar_matriz_piso(lista_pisos, patron_nuevo)
    else:
        print("No se han seleccionado patrones actual y nuevo.")


def mostrar_matriz_piso(piso, codigo_patron):
    # Mostrar la matriz del patrón en el piso dado
    print(f"Matriz del patrón en el piso {piso.nombre}:")
    piso.mostrar_matrices_piso(codigo_patron)




def menu():
    print("Menu:")
    print("1. Mostrar lista de pisos")
    print("2. Mostrar matrices de un piso")
    print("3. Cambiar patrones")
    print("4. Salir")

def main():
    ruta_archivo_xml = 'prueba.xml'
    lista_pisos = leer_archivo_xml(ruta_archivo_xml)

    gestor_patrones = GestorCodigosPatrones()  

    while True:
        menu()
        opcion = input("Ingrese el número de opción: ")

        if opcion == '1':
            mostrar_lista_pisos(lista_pisos)
        elif opcion == '2':
            mostrar_matrices_piso(lista_pisos, gestor_patrones)  
        elif opcion == '3':
            mostrar_patrones(gestor_patrones, lista_pisos)


        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
