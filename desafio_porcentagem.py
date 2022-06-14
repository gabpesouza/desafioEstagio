
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
outros = 19849.53

total = SP + RJ + MG + ES + outros

print(total)


def porcentagem(estado):
     calculo = (estado*100)/total
     print(str(calculo) + " % ")


porcentagem(RJ)
porcentagem(SP)
porcentagem(MG)
porcentagem(ES)
porcentagem(outros)
