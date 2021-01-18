def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " +  tipo_pesos  + " tienes?...")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas
1 - COP
2 - ARP
3 - MXP

ELIGE UNA OPCION: """

opcion = int(input(menu))
#ingresa como un string, por eso comillas
if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("ingresa una opcion correcta")

