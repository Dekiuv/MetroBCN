# Definir las conexiones (aristas) entre estaciones (líneas del metro)

aristas = {
    # Linea 1
    'Linea 1': [
        ('Urquinaona', 'Catalunya'),
        ('Catalunya', 'Universitat'),
        ('Universitat', 'Urgell'),
        ('Urgell', 'Rocafort'),
        ('Rocafort', 'Espanya')
    ],
    # Linea 2
    'Linea 2': [
        ('Paral·lel', 'Sant antoni'),
        ('Sant antoni', 'Universitat'),
        ('Universitat', 'Passeig de gracia'),
        ('Passeig de gracia', 'Tetuan'),
        ('Tetuan', 'Monumental'),
        ('Monumental', 'Sagrada familia'),
        ('Sagrada familia', 'Encants'),
        ('Encants', 'Clot'),
        ('Clot', 'Bac de roda'),
        ('Bac de roda', 'Sant marti'),
        ('Sant marti', 'La pau'),
        ('La pau', 'Verneda'),
        ('Verneda', 'Artigues sant adria'),
        ('Artigues sant adria', 'Sant roc'),
        ('Sant roc', 'Gorg'),
        ('Gorg', 'Pep ventura'),
        ('Pep ventura', 'Badalona pompeu fabra'),
    ],
    # Linea 3
    'Linea 3': [
        ('Trinitat nova', 'Roquetes'),
        ('Roquetes', 'Canyelles'),
        ('Canyelles', 'Valldaura'),
        ('Valldaura', 'Mundet'),
        ('Mundet', 'Montbau'),
        ('Montbau', "Vall d'hebron"),
        ("Vall d'hebron", 'Penitents'),
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
        ('Espanya', 'Tarragona'),
        ('Tarragona', 'Sants'),
        ('Sants', 'Plaça del centre'),
        ('Plaça del centre', 'Les corts'),
        ('Les corts', 'Maria cristina'),
        ('Maria cristina', 'Palau reial'),
        ('Palau reial', 'Zona universitaria')
    ],
    # Linea 4
    'Linea 4': [
        ('Verdaguer', 'Girona'),
        ('Girona', 'Passeig de gracia'),
        ('Passeig de gracia', 'Urquinaona'),
        ('Urquinaona', 'Jaume I'),
        ('Jaume I', 'Barceloneta'),
        ('Barceloneta', 'Ciutadella | vila olimpica'),
        ('Ciutadella | vila olimpica', 'Bogatell'),
        ('Bogatell', 'Llacuna'),
        ('Llacuna', 'Poblenou'),
        ('Poblenou', 'Selva de mar'),
        ('Selva de mar', 'El maresme forum'),
        ('El maresme forum', 'Besos mar'),
        ('Besos mar', 'Besos'),
        ('Besos', 'La pau'),
    ],
    # Linea 5
    'Linea 5': [
        ('Sants', 'Entença'),
        ('Entença', 'Hospital clinic'),
        ('Hospital clinic', 'Diagonal'),
        ('Diagonal', 'Verdaguer'),
        ('Verdaguer', 'Sagrada familia')
    ],
    # Linea 6
    'Linea 6': [
        ('Catalunya', 'Provenca'),
        ('Provenca', 'Gracia'),
        ('Gracia', 'Sant gervasi'),
        ('Sant gervasi', 'Muntaner'),
        ('Muntaner', 'La bonanova'),
        ('La bonanova', 'Les tres torres'),
        ('Les tres torres', 'Sarria')
    ],
    # Linea 7
    'Linea 7': [
        ('Gracia', 'Plaça molina'),
        ('Plaça molina', 'Padua'),
        ('Padua', 'El putxet'),
        ('El putxet', 'Tibidabo')
    ],
    # Linea 11
    'Linea 11': [
        ('Trinitat nova', "Casa de l'aigua"),
        ("Casa de l'aigua", 'Torre baró vallbona'),
        ('Torre baró vallbona', 'Ciutat meridiana'),
        ('Ciutat meridiana', 'Can cuias')
    ],
    # Linea 12
    'Linea 12': [
        ('Sarria', 'Reina elisenda')
    ]
}

def get_aristas():
    # Lista para almacenar las conexiones (aristas) sin líneas
    conexiones_sin_lineas = []

    # Recorrer el diccionario de aristas por línea
    for linea, conexiones_por_linea in aristas.items():
        # Añadir cada conexión (arista) a la lista de conexiones sin líneas
        for conexion in conexiones_por_linea:
            conexiones_sin_lineas.append(conexion)

    # Retornar la lista de conexiones sin líneas
    return conexiones_sin_lineas
#a