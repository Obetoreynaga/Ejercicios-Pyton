print("Calculadora con una sola variable")

print("***********************")
print("* Menu de opciones *")
print("***********************")

print("1. Suma \n" "2. Resta \n""3. Multiplicacion \n""4. Divicion \n""5. Divicion entera \n""6. Exponente \n""7. Modulo o resto \n")

num = int(input("Introduce la opcion deseada"))

if num == 1:
    print ("Elegiste suma \n")
    num = int(input("Solicita el 1er numero:"))
    num += int(input("Solicita el 2do numero:"))
    print ("El resultado de la suma es: ", num)

elif num == 2:
    print ("Elegiste resta \n")
    num = int(input("Solicita el 1er numero:"))
    num -= int(input("Solicita el 2do numero:"))
    print ("El resultado de la resta es: ", num )

elif num == 3:
    print ("Elegiste multiplicacion \n")
    num = int(input("Solicita el 1er numero:"))
    num *= int(input("Solicita el 2do numero:"))
    print ("El resultado de la multiplicacion es: ", num )

elif num == 4:
    print ("Elegiste division \n")
    num = float(input("Solicita el 1er numero:"))
    num /= float(input("Solicita el 2do numero:"))
    print ("El resultado de la divicion es: ", round (num , 2))

elif num == 5:
    print ("Elegiste divicion entera \n")
    num = int(input("Solicita el 1er numero:"))
    num //= int(input("Solicita el 2do numero:"))
    print ("El resultado de la divicion es: ", num ,)

elif num == 6:
    print ("Elegiste exponente \n")
    num = int(input("Solicita el 1er numero:"))
    num **= int(input("Solicita el 2do numero:"))
    print ("El resultado de la exponente es: ", num )

elif num == 7:
    print ("Elegiste modulo o resto \n")
    num = int(input("Solicita el 1er numero:"))
    num %= int(input("Solicita el 2do numero:"))
    print ("El modulo o resto es: ", num )

else:
    print("La opcion elegida no existe, vuelve a intentar")
