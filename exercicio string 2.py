frase = input("Escreva uma frase: ")
fraseNova = ""
for chr in frase:
    if chr != " ":
        fraseNova += chr.upper()
print("A frase contem", len(fraseNova), "letras")
