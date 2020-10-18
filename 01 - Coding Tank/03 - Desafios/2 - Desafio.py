#Declarando variáveis

frase = str(input("Digite uma frase ou palavra qualquer: "))
frase = list(frase)
#frase2 = frase
k = []
dic = {}

#Removendo duplicados

for i in range(len(frase)):
    if frase[i] not in k:
        k.append(frase[i])

#comparando com a primeira frase e adicionando ao dicionário, acumulando em uma variável toda vez q a letra se repete

for j in range(len(k)):
    qtd = 0
    for l in range(len(frase)):
        if k[j] == frase[l]:
            qtd = qtd+1
            dic[k[j]] = qtd

print(dic)