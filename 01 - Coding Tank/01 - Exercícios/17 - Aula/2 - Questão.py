import random

numeros_loto = []
for i in range(15):
  num = random.randint(1, 100)
  while num in numeros_loto:
    num = random.randint(1, 100)
  numeros_loto.append(num)

#print(numeros_loto)

num = 0
aposta = []
acertos = []
#num = int(input("Digite os números da sua aposta: "))

for j in range(15):
    num = (int(input("Digite um número da sua aposta: ")))
    if num < 1 or num > 100:
      print('Digite um número entre 1 e 100')
    else:
      if num in aposta:
        print('Este número já foi digitado')
      if num in numeros_loto:
        acertos.append(num)
        aposta.append(num)
      else:
        aposta.append(num)
    #num = int(input("Digite o próximo número: "))

qtd_acertos = len(acertos)

premio = {qtd_acertos == 15:'R$1.000.000,00 (1 milhão)',\
    qtd_acertos >=13 and qtd_acertos <=14 :'R$100.000,00 (100 mil)',\
    qtd_acertos >=10 and qtd_acertos <=12 :'R$2.000,00 (2 mil)',\
    qtd_acertos <10:'Sem premiação. =('}

#print(premio[len(acertos)])
print(premio[True])