import networkx as nx
import matplotlib.pyplot as plt

import estacion as es
import conexiones as co
import colores as col
import functions as func
    

# Crear un gráfico vacío
G = nx.Graph()

# Agregar nodos y aristas al gráfico
G.add_nodes_from(es.get_stations())
G.add_edges_from(co.get_aristas())


# Pedir las estaciones de inicio y fin al usuario
inicio, destino = func.menu_principal()
  
# Obtener el camino más corto entre las dos estaciones
ruta_mas_corta = nx.shortest_path(G, source=inicio, target=destino)

# Dibujar el gráfico
plt.figure(figsize=(8, 6))  # Ajustar el tamaño de la figura

# Dibujar las líneas (aristas)
for line, edges in co.aristas.items():
    for edge in edges:
        # Extraer las coordenadas de las estaciones
        estacion_1, estacion_2 = edge
        coord_1 = es.get_stations()[estacion_1]
        coord_2 = es.get_stations()[estacion_2]

        # Obtener el color de la línea usando el diccionario
        color = col.color_map.get(line)  # Devuelve None si la línea no existe en el mapa

        # Dibujar la línea entre las dos estaciones si el color existe
        if color is not None:
            plt.plot(*zip(coord_1, coord_2), color=color, alpha=0.8, linewidth=6)


# Dibujar los nodos (estaciones)
nx.draw_networkx_nodes(G, es.get_stations(), node_size=20, node_color=['white' if n in ruta_mas_corta else 'black' for n in G.nodes()])

# Título y ajuste de la visualización
plt.title(f'Ruta más rápida: {inicio} a {destino}', fontsize=14)
plt.grid(False)
plt.axis('off')  # Ocultar el eje
plt.show()
