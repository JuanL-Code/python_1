#Es palindromo o no
def palindromo(palabra):
    #Los espacios deben ser eliminados
    palabra = palabra.replace(" ","")
    #para que todas sean iguales
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    run()