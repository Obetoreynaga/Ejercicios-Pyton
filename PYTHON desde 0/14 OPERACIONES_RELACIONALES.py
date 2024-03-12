print("Introduce dos numeros a comparar: \n")

Primer_numero = int(input("Introduce el primer numero: "))
Segundo_numero = int(input("Introduce el segundo numero: "))

print("Los numero a comparar son : ", Primer_numero," y ", Segundo_numero, "\n")

if Primer_numero != Segundo_numero :
    print ("Es diferente...")
if Primer_numero < Segundo_numero :
    print ("Es menor...")
if Primer_numero > Segundo_numero :
    print ("Es mayor...")
if Primer_numero == Segundo_numero :
    print ("Es igual...")
if Primer_numero <= Segundo_numero :
    print ("Es igual o menor ...")
if Primer_numero >= Segundo_numero :
    print ("Es igual o mayor...")
else :
    print ("FIN")
