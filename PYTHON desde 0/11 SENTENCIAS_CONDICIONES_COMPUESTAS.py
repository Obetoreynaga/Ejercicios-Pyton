pokemon = 1

if pokemon == 3 :
    print("Es un pokemon Evolucionado")
if pokemon == 2 :
    print("Este pokemon puede evolucionar")

else :
    print("Es un pokemon no evolucionado ")
print("FIN")


print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿Cual es tu nombre?  ")

matematicas = float ( input (nombre + " ¿Cual es tu calificacion de matematicas?: "))
quimica = float ( input (nombre + " ¿Cual es tu calificacion de quimica?: "))
biologia = float ( input (nombre + " ¿Cual es tu calificacion de biologia?: "))

promedio = (matematicas + quimica + biologia) / 3

if promedio >= 6 :
    print ('Felicidades ' + nombre + ' "aprobaste" con un promedio de : ', promedio )
    print ('Felicidades ' + nombre + ' "aprobaste" con un promedio de : ', round (promedio,2 ))      

else:
    print ("Lo siento " + nombre + " reprobaste el curso con: ", promedio )
    print ("Lo siento " + nombre + " reprobaste el curso con: ", round (promedio,1 ))

print ("FIN.")
