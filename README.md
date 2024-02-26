# IPC2_Proyecto1_202100215
IPC2_Proyecto1_202100215
# Pisos de Guatemala, S.A.

Este es un proyecto para gestionar los patrones de azulejos de la empresa "Pisos de Guatemala, S.A.". El programa lee datos de patrones y pisos desde un archivo XML, permite realizar modificaciones en los patrones y calcular el costo mínimo para dichas modificaciones.

## Funcionalidades

- Cargar datos desde un archivo XML.
- Mostrar todos los pisos disponibles.
- Seleccionar un piso específico.
- Cambiar el patrón de un piso existente.
- Calcular el costo mínimo para modificar un patrón.
- Generar reportes gráficos de los patrones.

## Estructura del proyecto

El proyecto está dividido en los siguientes archivos y directorios:


- **main.py**: Punto de entrada principal del programa. Contiene la lógica de la interfaz de usuario ademas de que contiene funciones para cargar y manejar datos desde un archivo XML.
- **piso_manager.py**: Define la clase `Piso` y `ListaPisos` para manejar los datos de los pisos y sus patrones.
- **cost_calculator.py**: Contiene funciones para calcular el costo mínimo de modificar un patrón.
- **graph_generator.py**: Genera reportes gráficos de los patrones utilizando Graphviz.
- **prueba.xml**: Archivo de ejemplo que contiene datos de patrones y pisos en formato XML.

## Requisitos

- Python 3.x
- Bibliotecas estándar de Python: `xml.etree.ElementTree`, `argparse`

## Uso

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3 instalado.
3. Ejecuta `main.py` para iniciar el programa.
4. Sigue las instrucciones en pantalla para interactuar con el programa.
