#Ejemplo para Break
print ("while con al sentencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador  == 5:
        break
    print("Valor actual de la variante: ", contador)

print("Fin de programa, la sentencia break se ha ejecutado.")

#Ejemplo para continue

print ("\nwhile con al sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador  == 5:
        continue
    print("Valor actual de la variante: ", contador)
      
