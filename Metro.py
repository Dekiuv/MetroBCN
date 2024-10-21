import networkx as nx
import matplotlib.pyplot as plt

# Crear un gráfico vacío
G = nx.Graph()

# Definir las estaciones de la L6, L12 y L7 con sus coordenadas manualmente
estaciones = {
    #Linea 1
    'Universitat': (-0.003, 0.60),
    'Urgell': (-0.006, 0.60),
    'Rocafort': (-0.009, 0.60),
    'Espanya': (-0.012, 0.60),
    #Linea 2
    'Sant antoni': (-0.004, -0.20),
    'Passeig de gracia': (0.003, 0.60),
    'Tetuan': (0.007, 0.60),
    #Linea 3
    'Trinitat nova': (0.0185, 3.6),
    'Roquetes': (0.015, 3.6),
    'Canyelles': (0.012, 3.6),
    'Valldaura': (0.011, 4),
    'Mundet': (0.01, 4.4),
    'Montbau': (0.0075, 4.4),
    "Vall d'hebron": (0.005, 4.4),
    'Penitents': (0.004, 3.8),
    'Vallcarca': (0.0035, 3.4),
    'Lesseps': (0.0035, 2.75),
    'Fontana': (0.003, 2),
    'Diagonal': (0.003, 1.25),
    'Liceu': (0, -0.60),
    'Drassanes': (0, -1.70),
    'Paral·lel': (-0.004, -1),
    'Poble sec': (-0.008, -0.30),
    #Linea 6
    'Catalunya': (0, 0),
    'Provenca': (0, 1.5),
    'Gracia': (0, 2),    
    'Sant Gervasi': (-0.0010, 2.3),
    'Muntaner': (-0.0020, 2.6),  
    'La Bonanova': (-0.0030, 2.9),
    'Les tres torres': (-0.0040, 3.2),
    'Sarria': (-0.0050, 3.5),
    #Linea 7
    'Plaça Molina': (0, 2.5),
    'Padua': (0, 3),         
    'El Putxet': (0, 3.5),    
    'Tibidabo': (0, 4),
    #Linea 11
    "Casa de l'aigua": (0.02, 4),
    'Torre baró vallbona': (0.022, 4.5),         
    'Ciutat meridiana': (0.022, 5),    
    'Can cuias': (0.022, 5.5),
    #Linea 12
    'Reina Elisenda': (-0.0050, 4)
}

# Definir las conexiones (aristas) entre estaciones (líneas del metro)
aristas = [
    #Linea 1
    ('Catalunya', 'Universitat'),
    ('Universitat', 'Urgell'),
    ('Urgell', 'Rocafort'),
    ('Rocafort', 'Espanya'),
    #Linea 2
    ('Paral·lel', 'Sant antoni'),
    ('Sant antoni', 'Universitat'),
    ('Universitat', 'Passeig de gracia'),
    ('Passeig de gracia', 'Tetuan'),
    #Linea 3
    ('Trinitat nova', 'Roquetes'), 
    ('Roquetes', 'Canyelles'),
    ('Canyelles', 'Valldaura'),
    ('Valldaura', 'Mundet'),
    ('Mundet', 'Montbau'),
    ('Montbau', "Vall d'hebron"),
    ("Vall d'hebron", "Penitents"),
    ('Penitents', 'Vallcarca'),
    ('Vallcarca', 'Lesseps'),
    ('Lesseps', 'Fontana'),
    ('Fontana', 'Diagonal'),
    ('Diagonal', 'Passeig de gracia'),
    ('Passeig de gracia', 'Catalunya'),
    ('Catalunya', 'Liceu'),
    ('Liceu', 'Drassanes'),
    ('Drassanes', 'Paral·lel'),
    ('Paral·lel', 'Poble sec'),
    ('Poble sec', 'Espanya'),
    #Linea 6
    ('Catalunya', 'Provenca'),
    ('Provenca', 'Gracia'),    
    ('Gracia', 'Sant Gervasi'),
    ('Sant Gervasi', 'Muntaner'),
    ('Muntaner', 'La Bonanova'),
    ('La Bonanova', 'Les tres torres'),
    ('Les tres torres', 'Sarria'),
    #Linea 7
    ('Gracia', 'Plaça Molina'),  
    ('Plaça Molina', 'Padua'),    
    ('Padua', 'El Putxet'),       
    ('El Putxet', 'Tibidabo'),
    #Linea 11
    ('Trinitat nova', "Casa de l'aigua"),
    ("Casa de l'aigua", 'Torre baró vallbona'),
    ('Torre baró vallbona', 'Ciutat meridiana'),
    ('Ciutat meridiana', 'Can cuias'),
    #Linea 12
    ('Sarria', 'Reina Elisenda'),
]

# Colores para las líneas
line_color_L1 = 'red'  # Color para la L1
line_color_L2 = 'purple'  # Color para la L2
line_color_L3 = 'green'  # Color para la L2
line_color_L6 = '#7d84c6'  # Color para la L6
line_color_L7 = '#905010'   # Color para la L7
line_color_L11 = '#93C572'
line_color_L12 = '#c4c7e5'  # Color para la L12

# Agregar nodos y aristas al gráfico
G.add_nodes_from(estaciones)
G.add_edges_from(aristas)

# Dibujar el gráfico
plt.figure(figsize=(8, 6))  # Ajustar el tamaño de la figura

# Dibujar las líneas (aristas)
for edge in aristas:
    # L12
    if edge == ('Sarria', 'Reina Elisenda'):
        plt.plot(*zip(estaciones[edge[0]], estaciones[edge[1]]), color=line_color_L12, alpha=0.8, linewidth=6)
    # L11
    elif edge in [('Trinitat nova', "Casa de l'aigua"), ("Casa de l'aigua", 'Torre baró vallbona'), ('Torre baró vallbona', 'Ciutat meridiana'), ('Ciutat meridiana', 'Can cuias')]:
        plt.plot(*zip(estaciones[edge[0]], estaciones[edge[1]]), color=line_color_L11, alpha=0.8, linewidth=6)
    # L7
    elif edge in [('Gracia', 'Plaça Molina'), ('Plaça Molina', 'Padua'), ('Padua', 'El Putxet'), ('El Putxet', 'Tibidabo')]:
        plt.plot(*zip(estaciones[edge[0]], estaciones[edge[1]]), color=line_color_L7, alpha=0.8, linewidth=6)
    # L6
    elif edge in [('Catalunya', 'Provenca'), ('Provenca', 'Gracia'), ('Gracia', 'Sant Gervasi'), ('Sant Gervasi', 'Muntaner'), ('Muntaner', 'La Bonanova'), ('La Bonanova', 'Les tres torres'), ('Les tres torres', 'Sarria')]:
        plt.plot(*zip(estaciones[edge[0]], estaciones[edge[1]]), color=line_color_L6, alpha=0.8, linewidth=6)
    # L2
    elif edge in [('Paral·lel', 'Sant antoni'), ('Sant antoni', 'Universitat'), ('Universitat', 'Passeig de gracia'), ('Passeig de gracia', 'Tetuan')]:
        plt.plot(*zip(estaciones[edge[0]], estaciones[edge[1]]), color=line_color_L2, alpha=0.8, linewidth=6)
    # L3
    elif edge in [('Trinitat nova', 'Roquetes'), ('Roquetes', 'Canyelles'), ('Canyelles', 'Valldaura'),('Valldaura', 'Mundet'),('Mundet', 'Montbau'),('Montbau', "Vall d'hebron"),("Vall d'hebron", "Penitents"),('Penitents', 'Vallcarca'),('Vallcarca', 'Lesseps'),('Lesseps', 'Fontana'),('Fontana', 'Diagonal'),('Diagonal', 'Passeig de gracia'),('Passeig de gracia', 'Catalunya'),('Catalunya', 'Liceu'), ('Liceu', 'Drassanes'), ('Drassanes', 'Paral·lel'), ('Paral·lel', 'Poble sec'), ('Poble sec', 'Espanya')]:
        plt.plot(*zip(estaciones[edge[0]], estaciones[edge[1]]), color=line_color_L3, alpha=0.8, linewidth=6)
    # L1
    else:
        plt.plot(*zip(estaciones[edge[0]], estaciones[edge[1]]), color=line_color_L1, alpha=0.8, linewidth=6)

# Dibujar los nodos (estaciones)
nx.draw_networkx_nodes(G, estaciones, node_size=30, node_color='black')  # Tamaño ajustado y color de los nodos

# Título y ajuste de la visualización
plt.title('Metro de Barcelona', fontsize=14)
plt.grid(False)
plt.axis('off')  # Ocultar el eje
plt.show()
