def conversacion(mensaje):
    print("hola")
    print("como estas")
    print(mensaje)
    print("adios")

opcion = int(input("Elige una opcion"))
if opcion == 1:
    conversacion("elegiste la opcion 1")
elif opcion == 2 :
    conversacion("elegiste la opcion 2")
elif opcion == 3 :
    conversacion("elegiste la opcion 3")
else:
    print("escribe una opcion correcta")
    