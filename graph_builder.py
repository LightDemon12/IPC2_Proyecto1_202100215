from graph_builder import construir_matriz_nuevo

from graphviz import Digraph

def construir_matriz_nuevo(piso, codigo_patron=None):
    current_patron = piso.patrones_head
    while current_patron:
        if codigo_patron and current_patron.codigo != codigo_patron:
            current_patron = current_patron.siguiente
            continue

        print("Patron:", current_patron.codigo)
        current_patron_text = current_patron.patron
        index = 0

        # Crear el objeto Digraph
        dot = Digraph(comment='Patrón')

        # Agregar nodos al gráfico en el orden correcto de la matriz
        for i in range(piso.R):
            for j in range(piso.C):
                if index < len(current_patron_text):
                    if current_patron_text[index] == 'B':
                        dot.node(f'{i}-{j}', '', shape='square', style='filled', fillcolor='black', width='0.5')
                    elif current_patron_text[index] == 'N':
                        dot.node(f'{i}-{j}', '', shape='square', style='filled', fillcolor='white', width='0.5')
                    index += 1
                else:
                    dot.node(f'{i}-{j}', '', shape='square', style='filled', fillcolor='white', width='0.5')
        
        # Agregar bordes
        for i in range(piso.R):
            for j in range(piso.C):
                if j < piso.C - 1:
                    dot.edge(f'{i}-{j}', f'{i}-{j+1}', style='invis')
                if i < piso.R - 1:
                    dot.edge(f'{i}-{j}', f'{i+1}-{j}', style='invis')

        # Guardar el gráfico en formato DOT
        dot.render('patron', format='pdf', cleanup=True)

        if codigo_patron:
            break

        current_patron = current_patron.siguiente
