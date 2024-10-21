import networkx as nx
import matplotlib.pyplot as plt

import estacion as es
import conexiones as co
import colores as col

# Crear un gráfico vacío
G = nx.Graph()

# Agregar nodos y aristas al gráfico
G.add_nodes_from(es.estaciones)
G.add_edges_from(co.aristas)

# Pedir las estaciones de inicio y fin al usuario
inicio =  input("Escriba punto de inicio...")
destino = input("Escriba destino...")

# Obtener el camino más corto entre las dos estaciones
ruta_mas_corta = nx.shortest_path(G, source=inicio, target=destino)

# Dibujar el gráfico
plt.figure(figsize=(8, 6))  # Ajustar el tamaño de la figura

# Dibujar las líneas (aristas)
for edge in co.aristas:
    # L12
    if edge == ('Sarria', 'Reina Elisenda'):
        plt.plot(*zip(es.estaciones[edge[0]], es.estaciones[edge[1]]), color=col.line_color_L12, alpha=0.8, linewidth=6)
    # L11
    elif edge in [('Trinitat nova', "Casa de l'aigua"), ("Casa de l'aigua", 'Torre baró vallbona'), ('Torre baró vallbona', 'Ciutat meridiana'), ('Ciutat meridiana', 'Can cuias')]:
        plt.plot(*zip(es.estaciones[edge[0]], es.estaciones[edge[1]]), color=col.line_color_L11, alpha=0.8, linewidth=6)
    # L7
    elif edge in [('Gracia', 'Plaça Molina'), ('Plaça Molina', 'Padua'), ('Padua', 'El Putxet'), ('El Putxet', 'Tibidabo')]:
        plt.plot(*zip(es.estaciones[edge[0]], es.estaciones[edge[1]]), color=col.line_color_L7, alpha=0.8, linewidth=6)
    # L6
    elif edge in [('Catalunya', 'Provenca'), ('Provenca', 'Gracia'), ('Gracia', 'Sant Gervasi'), ('Sant Gervasi', 'Muntaner'), ('Muntaner', 'La Bonanova'), ('La Bonanova', 'Les tres torres'), ('Les tres torres', 'Sarria')]:
        plt.plot(*zip(es.estaciones[edge[0]], es.estaciones[edge[1]]), color=col.line_color_L6, alpha=0.8, linewidth=6)
    # L5
    elif edge in [('Sants', 'Entença'), ('Entença', 'Hospital clinic'), ('Hospital clinic', 'Diagonal'),]:
        plt.plot(*zip(es.estaciones[edge[0]], es.estaciones[edge[1]]), color=col.line_color_L5, alpha=0.8, linewidth=6)
    # L4
    elif edge in [('Passeig de gracia', 'Urquinaona'),]:
        plt.plot(*zip(es.estaciones[edge[0]], es.estaciones[edge[1]]), color=col.line_color_L4, alpha=0.8, linewidth=6)
    # L3
    elif edge in [('Trinitat nova', 'Roquetes'), ('Roquetes', 'Canyelles'), ('Canyelles', 'Valldaura'),('Valldaura', 'Mundet'),('Mundet', 'Montbau'),('Montbau', "Vall d'hebron"),("Vall d'hebron", "Penitents"),('Penitents', 'Vallcarca'),('Vallcarca', 'Lesseps'),('Lesseps', 'Fontana'),('Fontana', 'Diagonal'),('Diagonal', 'Passeig de gracia'),('Passeig de gracia', 'Catalunya'),('Catalunya', 'Liceu'), ('Liceu', 'Drassanes'), ('Drassanes', 'Paral·lel'), ('Paral·lel', 'Poble sec'), ('Poble sec', 'Espanya'), ('Espanya', 'Tarragona'), ('Tarragona', 'Sants'), ('Sants', 'Plaça del centre'), ('Plaça del centre', 'Les corts'), ('Les corts', 'Maria cristina'), ('Maria cristina', 'Palau reial'), ('Palau reial', 'Zona universitaria')]:
        plt.plot(*zip(es.estaciones[edge[0]], es.estaciones[edge[1]]), color=col.line_color_L3, alpha=0.8, linewidth=6)
    # L2
    elif edge in [('Paral·lel', 'Sant antoni'), ('Sant antoni', 'Universitat'), ('Universitat', 'Passeig de gracia'), ('Passeig de gracia', 'Tetuan')]:
        plt.plot(*zip(es.estaciones[edge[0]], es.estaciones[edge[1]]), color=col.line_color_L2, alpha=0.8, linewidth=6)
    # L1
    else:
        plt.plot(*zip(es.estaciones[edge[0]], es.estaciones[edge[1]]), color=col.line_color_L1, alpha=0.8, linewidth=6)

# Dibujar los nodos (estaciones)
nx.draw_networkx_nodes(G, es.estaciones, node_size=20, node_color=['white' if n in ruta_mas_corta else 'black' for n in G.nodes()])

# Título y ajuste de la visualización
plt.title(f'Ruta más rápida: {inicio} a {destino}', fontsize=14)
plt.grid(False)
plt.axis('off')  # Ocultar el eje
plt.show()
