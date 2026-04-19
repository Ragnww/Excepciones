inventarioZ = [
    {"talla": 38, "color": "negro", "tipo": "deportivo"},
    {"talla": 39, "color": "blanco", "tipo": "casual"},
    {"talla": 40, "color": "negro", "tipo": "formal"},
    {"talla": 41, "color": "azul", "tipo": "deportivo"},
    {"talla": 42, "color": "rojo", "tipo": "casual"},
    {"talla": 38, "color": "blanco", "tipo": "formal"},
    {"talla": 39, "color": "negro", "tipo": "deportivo"},
    {"talla": 40, "color": "gris", "tipo": "casual"}
]

class inventarioError(Exception):
    pass

def buscarProducto(producto,inventario):
    try:
        producto[0] = int(producto[0])
        producto[1] = producto[1].lower()
        producto[2] = producto[2].lower()
        for zapato in inventario:
            if (zapato["talla"] == producto[0]) and (zapato["color"] == producto[1]) and (zapato["tipo"] == producto[2]):
                print("Zapato encontrado")
                print(f"Zapato talla {zapato['talla']} color {zapato['color']} y tipo {zapato['tipo']} disponible")
                break
        else:
            raise inventarioError("Zapato no encontrado")
    except ValueError:
        print ("Talla Invalida")
    except inventarioError as e:
        print(e)

talla = input("Cual es la talla que esta buscando: ")
color = input("Cual es el color que esta buscando: ")
tipo = input("Cual es el tipo que esta buscando: ")
busquedaU = [talla,color,tipo]
buscarProducto(busquedaU,inventarioZ)
    