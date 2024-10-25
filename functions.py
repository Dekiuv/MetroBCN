
import estacion as es



def solicitar_estacion(mensaje, estaciones):
    while True:
        estacion = input(mensaje)
        if estacion in estaciones:
            print("Estación encontrada")
            return estacion
        else:
            print("Estación no encontrada, inténtelo de nuevo.")

def menu_principal():
    # Obtener la lista de estaciones
    estaciones = es.get_stations()

    # Mostrar el menú
    while True:
        print("\nEstaciones disponibles:")
        for estacion in estaciones:
            print(estacion)

        # Solicitar el punto de inicio
        inicio = solicitar_estacion("Escriba el punto de inicio: ", estaciones)

        # Solicitar el destino
        destino = solicitar_estacion("Escriba el destino: ", estaciones)

        # Confirmar el inicio y destino ingresados
        print(f"\nRuta seleccionada: {inicio} -> {destino}")
        
        # Salir del menú principal
        return inicio, destino