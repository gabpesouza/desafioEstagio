import json

with open("dados.json" , "r", encoding="utf-8") as arquivo:

        conteudo = json.load(arquivo)
menor = 0
maior = 0

#Descobrindo maior e menor valor faturado
for x in conteudo :
    if x["valor"] > maior:
        maior = x["valor"]
    if x["valor"] <= menor:
        menor = x["valor"]




print("maior valor : " + str(maior))
print("menor valor : " + str(menor))


#Verificando dias úteis
feriados =[]
for x in conteudo:
        if x["valor"] == 0 :
                feriados.append(x["dia"])

diasUteis = 30 - len(feriados)

print(diasUteis)




#Media mensal
somatotal = 0
for x in conteudo :
    somatotal = x["valor"] + somatotal

mediaMensal = somatotal/diasUteis

print(mediaMensal)

#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
numeroDias = []
for x in conteudo :
          if x["valor"] > mediaMensal :
                  numeroDias.append(x["dia"])

print(numeroDias)

numeroDiasFaturados = len(numeroDias)
print(numeroDiasFaturados)