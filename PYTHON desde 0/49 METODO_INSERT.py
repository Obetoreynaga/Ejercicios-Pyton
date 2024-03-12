print("Lista original")
letters = ["b", "d", "f", "g"]
print(f"Lista: (letters)")

print("\nInsertado 'a' en posicion 0")
letters.insert(0, 'a')
print(f"Lista: {letters}")

print("\nInsertado 'c' en posicion 2")
letters.insert(2, 'c')
print(f"Lista: {letters}")

print("\nInsertado 'e' en posicion 4")
letters.insert(4, 'e')
print(f"Lista: {letters}")

print("\nInsertado 'z' en posicion 100")
letters.insert(100, 'z')
print(f"Lista: {letters}")