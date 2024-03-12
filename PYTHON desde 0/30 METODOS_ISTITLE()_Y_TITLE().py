primer_nombre = input("Nombre: ")
apellido = input("Apellido: ")
nombre_completo = f"{primer_nombre} {apellido}"

print()
print(f"El formato del metodo title() se a aplicado?: {nombre_completo.istitle() }")
print(f"Aplicando el metodo title(): {nombre_completo.title ()}")
print(f"Volvemos a  imprimirel metodo: {nombre_completo} ")

print()
nombre_completo = nombre_completo.title()
print(f"El formato del metodo title() se a aplicado?: {nombre_completo.istitle() }")
print(f"Se ha aplicado el metodo title() de manera permanente: {nombre_completo}")
