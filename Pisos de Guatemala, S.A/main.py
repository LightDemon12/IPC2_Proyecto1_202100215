import xml.etree.ElementTree as ET 
from xml.dom import minidom 

def main ():
    print("Bienvenido a Pisos de Guatemala, S.A.")
    print("=======================================")
    while True:
       print("Menú principal") 
       print("1. Mostrar todos los pisos disponibles")
       print("2. Seleccionar un piso")
       print("3. Salir")

       opcion = int(input("Ingrese la opción que desea: "))
       if opcion == 1:
           print("Mostrar todos los pisos disponibles")
       elif opcion == 2:
           print("Seleccionar un piso:")      
       elif opcion == 3:
            print("¡Hasta luego!")      
            break
       else:
            print("Opción inválida")
   
if __name__ == "__main__":
   main()