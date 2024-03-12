print("************************" )
print("**Ejercicio practico 1** " )
print("************************ \n" )

name = input("Ingresa tu nombre:  ")
clave = int(input("Ingresa tu clave:  "))
year = float(input("Ingresa años de antiguedad:  "))

if clave == 1:
    if year >= 1 and year < 2:
        print("El empleado ", name, "Tienes 6 dias de vacaciones.")
    elif year >=2 and year <= 6:
        print("El empleado ", name, "Tienes 14 dias de vacaciones.")
    elif year >=7:
        print("El empleado ", name, "Tienes 20 dias de vacaciones.")
    else:
        print("El empleado ", name, "aun no tiene derecho a  vacaciones.")

elif clave == 2 :
    if year >= 1 and year < 2:
        print("El empleado ", name, "Tienes 7 dias de vacaciones.")
    elif year >=2 and year <= 6:
        print("El empleado ", name, "Tienes 15 dias de vacaciones.")
    elif year >=7:
        print("El empleado ", name, "Tienes 22 dias de vacaciones.")
    else:
        print("El empleado ", name, "aun no tiene derecho a  vacaciones.")

elif clave == 3 :
    if year >= 1 and year < 2:
        print("El empleado ", name, "Tienes 10 dias de vacaciones.")
    elif year >=2 and year <= 6:
        print("El empleado ", name, "Tienes 20 dias de vacaciones.")
    elif year >=7:
        print("El empleado ", name, "Tienes 30 dias de vacaciones.")
    else:
        print("El empleado ", name, "aun no tiene derecho a  vacaciones.")

else :
    print("Clave no existe.")BaseException
