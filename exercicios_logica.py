A = [1,3,5,7]

i = 1

for x in range(0,10) :
    i = i + 2
    print(i)
print("=-" * 30)

B = [2, 4, 8, 16, 32, 64]
i = 2
for x in range(0,10) :
        i = i * 2
        print(i)
print("=-" * 30)

C = [0, 1, 4, 9, 16, 25, 36]
i = 1
y = 3
for x in range(0,10):
    i = i + y
    y = y + 2
    print(i)
print("=-" * 30)

D = [4, 16, 36, 64]



atual = 2
proximo =  atual*atual
multiplicador = atual + 2
for x in range(0,10) :
    proximo = atual*atual
    multiplicador = atual +  2
    atual = multiplicador
    print(proximo)
print("=-" * 30)

E = [1, 1, 2, 3, 5, 8]

anterior = 1
proximo = 1
soma = anterior + proximo

for x in range(0,10) :
    soma = anterior + proximo
    anterior = proximo
    proximo = soma
    print(soma)





