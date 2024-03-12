string = "0123456789"
substring = ""

print(f"Cadena principal: {string}")

substring = string[0]
print(f"\nSubcadenacon indice en la posicion [0] es: {substring}")

substring = string[5]
print(f"\nSubcadenacon indice en la posicion [5] es: {substring}")

substring = string[4]
print(f"\nSubcadenacon indice en la poscion [4] es: {substring}")

substring = string[0:3]
print(f"\nSubcadenacon indice en la posicion [0:3] es: {substring}")

substring = string[:3]
print(f"\nSubcadenacon indice en la posicion [:3] es: {substring}")

substring = string[5:]
print(f"\nSubcadenacon indice en la posicion [5:] es: {substring}")

substring = string[-4:-1]
print(f"\nSubcadenacon indice en la posicion [-4:-1] es: {substring}")
