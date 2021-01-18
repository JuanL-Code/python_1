import random
def generar_contrasena():
    #4 listas de simbolos a combinar
    mayusculas = ["A", "B", "C", "D", "E","F", "G"]
    minusculas = ["a", "b", "c", "d", "e","f", "g"]
    simbolos = ["!", "#", "$", "&", "/","(", ")"]
    numeros = ["1", "2" "3", "4", "5","6", "7", "8", "9", "0"]

    caracteres = mayusculas + minusculas + simbolos + numeros


    #al azar de la lista caracteres
    contrasena = []


    for i in range (15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    #generar un string de mi lista original
    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print("tu nueva contraseña es: " + contrasena)

if __name__ == "__main__":
    run()