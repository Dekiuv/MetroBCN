# Definir las estaciones

estaciones = {
    # Linea 1
    'Linea 1': {
        'Urquinaona': (0.003, -0.60),
        'Universitat': (-0.003, 0.60),
        'Urgell': (-0.006, 0.60),
        'Rocafort': (-0.009, 0.60),
        'Espanya': (-0.013, 0.60)
    },
    # Linea 2
    'Linea 2': {
        'Sant antoni': (-0.004, -0.20),
        'Passeig de gracia': (0.003, 0.60),
        'Tetuan': (0.007, 0.60),
        'Monumental': (0.0085, 0.90),
        'Sagrada familia': (0.01, 1.25),
        'Encants': (0.013, 1.25),
        'Clot': (0.015, 1.25),
        'Bac de roda': (0.017, 1.25),
        'Sant marti': (0.019, 1.25),
        'La pau': (0.021, 1.25),
        'Verneda': (0.023, 1.25),
        'Artigues sant adria': (0.025, 1.25),
        'Sant roc': (0.027, 0.7),
        'Gorg': (0.029, 0.7),
        'Pep ventura': (0.031, 0.7),
        'Badalona pompeu fabra': (0.033, 0.7),
    },
    # Linea 3
    'Linea 3': {
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
        'Tarragona': (-0.013, 0.90),
        'Sants': (-0.013, 1.25),
        'Plaça del centre': (-0.013, 2.3),
        'Les corts': (-0.013, 2.9),
        'Maria cristina': (-0.013, 3.5),
        'Palau reial': (-0.015, 4),
        'Zona universitaria': (-0.017, 4.5)
    },
    # Linea 4
    'Linea 4': {
        'Girona': (0.005, 0.95),
        'Jaume I': (0.003, -1.2),
        'Barceloneta': (0.003, -1.7),
        'Ciutadella | vila olimpica': (0.007, -1.7),
        'Bogatell': (0.0085, -1.2),
        'Llacuna': (0.011, -1.2),
        'Poblenou': (0.014, -1.2),
        'Selva de mar': (0.018, -1.2),
        'El maresme forum': (0.021, -1.2),
        'Besos mar': (0.021, -0.35),
        'Besos': (0.021, 0.60),
    },
    # Linea 5
    'Linea 5': {
        'Entença': (-0.009, 1.25),
        'Hospital clinic': (-0.0045, 1.25),
        'Verdaguer': (0.0065, 1.25),
    },
    # Linea 6
    'Linea 6': {
        'Catalunya': (0, 0),
        'Provenca': (0, 1.5),
        'Gracia': (0, 2),
        'Sant gervasi': (-0.0010, 2.3),
        'Muntaner': (-0.0020, 2.6),
        'La bonanova': (-0.0030, 2.9),
        'Les tres torres': (-0.0040, 3.2),
        'Sarria': (-0.0050, 3.5)
    },
    # Linea 7
    'Linea 7': {
        'Plaça molina': (0, 2.5),
        'Padua': (0, 3),
        'El putxet': (0, 3.5),
        'Tibidabo': (0, 4)
    },
    # Linea 11
    'Linea 11': {
        "Casa de l'aigua": (0.02, 4),
        'Torre baró vallbona': (0.022, 4.5),
        'Ciutat meridiana': (0.022, 5),
        'Can cuias': (0.022, 5.5)
    },
    # Linea 12
    'Linea 12': {
        'Reina elisenda': (-0.0050, 4)
    }
}

def get_stations():
    # Diccionario para almacenar las estaciones sin líneas
    estaciones_sin_lineas = {}

    # Recorrer el diccionario de estaciones por línea
    for linea, estaciones_por_linea in estaciones.items():
        # Recorrer cada estación en la línea
        for estacion, coordenadas in estaciones_por_linea.items():
            # Añadir la estación y sus coordenadas al nuevo diccionario
            estaciones_sin_lineas[estacion] = coordenadas

    # Imprimir el nuevo diccionario de estaciones sin líneas
    return estaciones_sin_lineas