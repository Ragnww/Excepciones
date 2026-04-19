class archivoError(Exception):
    pass

def guardarPalabras():
    try:
        palabras = []
        for i in range(10):
            palabra = input(f"Ingrese la palabra {i+1}: ")
            if palabra == "":
                raise archivoError("No se permiten palabras vacías")
            palabras.append(palabra.lower())

        with open("palabras.txt", "w") as archivo:
            for p in palabras:
                archivo.write(p + "\n")
        print("Palabras guardadas correctamente en palabras.txt")

    except archivoError as e:
        print(f"Error: {e}")
    except Exception:
        print("Ocurrió un error al manejar el archivo")

guardarPalabras()