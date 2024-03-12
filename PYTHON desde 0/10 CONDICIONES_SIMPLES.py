num_uno = 5

if num_uno == 5 :
    print("El numero es cinco")

print("Fin")

print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿Cual es tu nombre?,  ")

matematicas = int ( input (nombre + " ¿Cual es tu calificacion de matematicas?: "))
quimica = int ( input (nombre + " ¿Cual es tu calificacion de quimica?: "))
biologia = int ( input (nombre + " ¿Cual es tu calificacion de biologia?: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6 :
    print ('Felicidades ' + nombre + ' "aprobaste" con un promedio de : ', promedio )

print ("FIN.")



