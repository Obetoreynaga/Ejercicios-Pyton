numeros = []
longitud_lista = int(input("¿Cuantos numeros contendra la lista?: "))

for _ in range(longitud_lista) :
    numeros.append(int(input("Introduce un numero entero: ")))

print(f"\nLista: {numeros} \nLa suma total de los elementos es: {sum(numeros)}")


