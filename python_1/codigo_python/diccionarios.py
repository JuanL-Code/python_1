def run():
    mi_diccionario = {
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3,    
    }
    #imprimir contenido
    #print(mi_diccionario["llave1"])
    #print(mi_diccionario["llave2"])
    #print(mi_diccionario["llave3"])

    poblacion_paises = {
        "argentina" : 500000000,
        "brasil" : 60000000,
        "colombia" : 70000000
    }

    for pais in poblacion_paises.keys():
        print (pais)

    for pais in poblacion_paises.values():
        print (pais) 

    for pais, poblacion in poblacion_paises.items():
        print (pais + " tiene " + str(poblacion) + " habitantes") 
    

if __name__ == "__main__":
    run()


    