menu = """
Bienvenido al conversor de monedas
1 - COP
2 - ARP
3 - MXP

ELIGE UNA OPCION: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Ingresa la cantidad de COP a convertir...")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("Ingresa la cantidad de ARP a convertir...")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("Ingresa la cantidad de MXP a convertir...")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print("ingresa una opcion correcta")

