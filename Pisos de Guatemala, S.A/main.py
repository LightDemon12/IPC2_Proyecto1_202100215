import xml.etree.ElementTree as ET 
from xml.dom import minidom
from patterns import Patron
from piso_manager import Piso

def main():
    print("Bienvenido a Pisos de Guatemala, S.A.")
    print("=======================================")
    while True:
        print("Menú principal") 
        print("1. Mostrar todos los pisos disponibles")
        print("2. Seleccionar un piso")
        print("3. Salir")

        opcion = int(input("Ingrese la opción que desea: "))
        return opcion

def xml_rutaET(ruta_archivo_xml):
    tree = ET.parse(ruta_archivo_xml)
    root = tree.getroot()
    
    for Piso_elem in root.findall('piso'):
        nombre = piso.find('nombre').text
        R = piso.find('R').text
        C = piso.find('C').text
        F = piso.find('F').text
        S = piso.find('S').text
        piso = Piso(nombre, R, C, F, S)
        for patron in piso.findall('patron'):
            codigo = patron.find('codigo').text
            patron = patron.find('patron').text
            piso.patrones = Patron(codigo, patron)
        piso.siguiente = piso
        print(piso.nombre, piso.R, piso.C, piso.F, piso.S, piso.patrones, piso.siguiente)

if __name__ == "__main__":
    opcion = 0
    ruta_archivo_xml = 'prueba.xml'
    while opcion != 6:
        opcion = main()
        if opcion == 1:
            print( ruta_archivo_xml)
      

        elif opcion == 2:
            print('')
           

        elif opcion == 3:
            print('')
           

        elif opcion == 4:
            print('')
          

        elif opcion == 5:
          
            print('Datos limpios')
        
        elif opcion == 6:
            print('Adiós!')
            break
        else:
            print('Opción no válida')
        print('')
    main()
