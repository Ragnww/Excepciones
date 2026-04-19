class correoInvalido(Exception):
    pass

correoU = input("Ingrese su correo: ")


def verificarCorreo(correo):
    try:
        if len(correo.split())>1:
            raise correoInvalido("Un correo no puede llevar espacios")
        if correo.count("@") != 1:
            raise correoInvalido("Un correo tiene que llevar un solo @")
        usuario, dominio = correo.split("@")
        if usuario == "":
            raise correoInvalido("Falta el usuario antes del @")
        if dominio == "":
            raise correoInvalido("Falta el dominio después del @")
        if not ("." in dominio):
            raise correoInvalido("El dominio esta mal")
        if dominio.startswith(".") or dominio.endswith("."):
            raise correoInvalido("El dominio no puede empezar o terminar con punto")
        print("Tu correo es valido")
    except correoInvalido as e:
        print(f"Correo inválido: {e}")

verificarCorreo(correoU)