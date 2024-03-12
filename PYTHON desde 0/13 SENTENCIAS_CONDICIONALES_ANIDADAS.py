print("==============================")
print("¡¡¡Convertido de numero a tipo de pokemon!!!")
print("==============================")

print ("Menu de opciones: \n")

print("Presiona 1 para convertir de numero a pokemon.")
print("Presiona 2 para convertir de pokemon a numero \n.")

opcion = int(input("¿Cual es tu opcion deseada?: "))

if opcion == 1:
    print("\n Conversor de numero a pokemon. \n")

    opcion_uno = int(input("¿Cual es el numero que desas converir a pokemon?: "))

    if opcion == 1 :
            print("Es tipo fuego")
    elif opcion == 2 :
            print("Es tipo agua")
    elif opcion == 3 :
            print("Es tipo  hierva")
    elif opcion == 4 :
            print("Es tipo  electrico")
    elif opcion == 5 :
            print("Es tipo  roca")
    elif opcion == 6 :
            print("Es tipo  fantasma")
    elif opcion == 7 :
            print("Es tipo bicho")
    else :
            print("No hay mas tipos")



elif opcion == 2:
    print("\n Conversor de pokemon a numero. \n")

    opcion_dos = input("¿Cual es el pokemon que deseas convertir a numero?")
    opcion_dos = opcion_dos.lower()
    
    if opcion == "fuego" :
            print("Es numero es 1")
    elif opcion == "agua" :
            print("Es numero es 2")
    elif opcion == "hierva" :
            print("Es numero es 3")
    elif opcion == "electrico" :
            print("Es numero es 4")
    elif opcion == "roca" :
            print("Es numero es 5")
    elif opcion == "fantasma" :
            print("Es numero es 6")
    elif opcion == "bicho" :
            print("Es numero es 7")
    else :
            print("No hay mas tipos")
            
else:
        print("Opcion no disponible.")

