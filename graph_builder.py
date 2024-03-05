import graphviz

def generate_afd():
    # Creamos el objeto Digraph de Graphviz
    dot = graphviz.Digraph()

    # Añadimos los nodos al grafo
    dot.node("inicio", label="Inicio", shape="circle", color="black", style="filled")
    dot.node("numero", label="Numero", shape="circle", color="black", style="filled")
    dot.node("punto", label=".", shape="circle", color="black", style="filled")
    dot.node("coma", label=",", shape="circle", color="black", style="filled")
    dot.node("tres_numeros", label="Tres\nNúmeros", shape="doublecircle", color="black", style="filled")

    # Añadimos las transiciones
    dot.edge("inicio", "numero", label="[+-0-9]")
    dot.edge("numero", "punto", label="[.]")
    dot.edge("punto", "tres_numeros", label="[0-9]")
    dot.edge("tres_numeros", "coma", label="[,]")
    dot.edge("coma", "numero", label="[0-9]")
    dot.edge("tres_numeros", "punto", label="[.]")
    dot.edge("coma", "punto", label="[.]")

    # Renderizamos el grafo y lo guardamos como imagen
    dot.render("afd_valid", format="png")

if __name__ == "__main__":
    generate_afd()
