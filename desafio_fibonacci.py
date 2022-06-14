numero = int(input("Digite o numero que quer saber se pertence a sequencia fibonacci"))
anterior = 0
proximo = 1
fibonacci = False

for x in range(0,numero+1):
        soma = anterior + proximo
        anterior = proximo
        proximo = soma
        print(soma)


        if numero == soma:
                fibonacci = True

if fibonacci == True:
    print("O numero pertence a sequencia")
else:
    print("O numero nao pertence a sequencia")


