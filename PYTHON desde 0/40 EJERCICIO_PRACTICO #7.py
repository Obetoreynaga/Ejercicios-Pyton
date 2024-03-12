string = input("Introduce un string para invertirlo: ")
string_reversed = ""

for character in string:
    string_reversed = character + string_reversed


print(string_reversed)
