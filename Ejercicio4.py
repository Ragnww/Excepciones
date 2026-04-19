def calcularNomina():
    try:
        limite = (1750905) * 2
        salario = int(input("Ingrese su salario: "))
        if salario <= 0:
            raise ValueError
        pagoQuincenal = salario / 2
        if salario < limite:
            auxilio = 249095 / 2
        else:
            auxilio = 0
        nomina = pagoQuincenal + auxilio
        print(f"Sueldo mensual: {salario}")
        print(f"Pago quincenal: {pagoQuincenal}")
        print(f"Auxilio transporte: {auxilio}")
        print(f"Total a pagar: {nomina}")
    except ValueError:
         print("salario invalido")

calcularNomina()