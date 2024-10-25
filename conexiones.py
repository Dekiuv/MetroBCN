# Definir las conexiones (aristas) entre estaciones (líneas del metro)

aristas = {
    # Linea 1
    'Linea 1': [
        ('Urquinaona', 'Catalunya'),
        ('Catalunya', 'Universitat'),
        ('Universitat', 'Urgell'),
        ('Urgell', 'Rocafort'),
        ('Rocafort', 'Espanya'),
        ('Espanya', 'Hostafrancs'),
        ('Hostafrancs', 'Plaça de sants'),
        ('Plaça de sants', 'Mercat nou'),
        ('Mercat nou', 'Santa eulalia'),
        ('Santa eulalia', 'Torrassa'),
        ('Torrassa', 'Florida'),
        ('Florida', 'Can serra'),
        ('Can serra', 'Rambla just oliveras'),
        ('Rambla just oliveras', 'Av. carrilet'),
        ('Av. carrilet', 'Bellvitge'),
        ('Bellvitge', 'Hospital de bellvitge'),
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
        ("Trinitat nova", 'Via julia'),
        ('Via julia', 'Llucmajor'),
        ('Llucmajor', 'Maragall'),
        ('Maragall', 'Guinardo hospital de sant pau'),
        ('Guinardo hospital de sant pau', 'Alfons X'),
        ('Alfons X', 'Joanic'),
        ('Joanic', 'Verdaguer'),
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
        ('Cornella centre', 'Gavarra'),
        ('Gavarra', 'Sant ildefons'),
        ('Sant ildefons', 'Can boixeres'),
        ('Can boixeres', 'Can vidalet'),
        ('Can vidalet', 'Pubilla cases'),
        ('Pubilla cases', 'Ernest lluch'),
        ('Ernest lluch', 'Collblanc'),
        ('Collblanc', 'Badal'),
        ('Badal', 'Plaça de sants'),
        ('Plaça de sants', 'Sants'),
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
    # Linea 8
    'Linea 8': [
        ('Espanya', 'Magoria la campana'),
        ('Magoria la campana', 'Ildefons cerda'),
        ('Ildefons cerda', 'Europa fira'),
        ('Europa fira', 'Gornal'),
        ('Gornal', 'Sant josep'),
        ('Sant josep', 'Av. carrilet'),
        ('Av. carrilet', 'Almeda'),
        ('Almeda', 'Cornella riera'),
        ('Cornella riera', 'Sant boi'),
    ],
    # Linea 10
    'Linea 10': [
        ('Collblanc', 'Torrassa'),
        ('Torrassa', 'Can tries gornal'),
        ('Can tries gornal', 'Provençana'),
        ('Provençana', 'Ciutat de la justicia'),
        ('Ildefons cerda', 'Ciutat de la justicia'),
        ('Ciutat de la justicia', 'Foneria'),
        ('Foneria', 'Foc'),
        ('Foc', 'Zona franca'),
        ('Zona franca', 'Port comercial la factoria'),
        ('Port comercial la factoria', 'Ecoparc'),
        ('Ecoparc', 'Zal | riu vell'),
    ],
    # Linea 9
    'Linea 9': [
        ('Zona universitaria', 'Collblanc'),
        ('Collblanc', 'Torrassa'),
        ('Torrassa', 'Can tries gornal'),
        ('Can tries gornal', 'Europa fira'),
        ('Europa fira', 'Fira'),
        ('Fira', 'Parc logistic'),
        ('Parc logistic', 'Mercabarna'),
        ('Mercabarna', 'Les moreres'),
        ('Les moreres', 'El prat estacio'),
        ('El prat estacio', 'Centric'),
        ('Centric', 'Parc nou'),
        ('Parc nou', 'Mas blau'),
        ('Mas blau', 'Aeroport T2'),
        ('Aeroport T2', 'Aeroport T1'),
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