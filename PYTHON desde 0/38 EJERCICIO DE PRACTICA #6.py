frase = input("Introduca una frase: ")
palabra =  input("Introduce la palabra que desea eliminar: ")
substring = ""

inicio = frase.find (palabra)
substring = frase[0:inicio] + frase[inicio + len(palabra) +1 : ]
print (f"Cadena resultante: {substring}")
