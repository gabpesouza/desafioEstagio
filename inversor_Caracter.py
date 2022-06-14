
caracteres = []
caracteresInvertido =[]



numeroLetras = int(input("Quantas letras tem a palavra que vai digitar?"))

for x in range(0,numeroLetras):
    caracteres.append(input("digite a " + str(x+1) + " letra "))
print(caracteres)

indice = numeroLetras - 1

while len(caracteresInvertido) != len(caracteres):
    caracteresInvertido.append(caracteres[indice])
    indice = indice - 1

print(caracteresInvertido)



