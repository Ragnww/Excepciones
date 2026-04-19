from datetime import datetime

hoy = datetime.now().date()

class fechaInvalida(Exception):
    pass

def buscarEdad():
    try:
        year = int(input("Ingrese su año de nacimiento: "))
        mes = int(input("Ingrese su mes de nacimiento: "))
        dia = int(input("Ingrese su dia de nacimiento: "))
        fechaN = f"{year}-{mes}-{dia}"
        fecha_valida = datetime.strptime(fechaN, "%Y-%m-%d").date()
        if fecha_valida > hoy:
            raise fechaInvalida("Esa fecha no ha pasado")
        edad = hoy.year - year
        if (mes, dia) > (hoy.month, hoy.day):
            edad -= 1
        print(f"Tienes {edad} años")
        
    except ValueError:
        print("Fecha invalida")
    except fechaInvalida as e:
        print(e)

buscarEdad()
