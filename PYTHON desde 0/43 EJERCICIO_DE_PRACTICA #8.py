numero = int(input("¿Que tabla de multiplicar quieres ver?: "))
for tabla in range(11):
    print(numero, "x", tabla, "=", numero * tabla)

numero = int(input("¿Que tabla de multiplicar quieres ver?: "))
for tabla in range(11):
    print(f"{numero} x {tabla} = {numero * tabla}")
