idade = [24, 23, 22, 22, 23, 25, 18, 35, 28, 30]
altura = [1.82, 1.80, 1.78, 1.90 ,1.88, 1.93, 1.75, 1.99, 1.70, 1.66]
maior = 0.0
i = 0

while i < 8:
    if altura[i] > altura[i+1] and altura[i] > maior:
        maior = altura[i]
    i = i+1
if maior < altura[9]:
    maior = altura[9]

jogador = idade[altura.index(maior)]
print('A idade do maior é:', jogador)