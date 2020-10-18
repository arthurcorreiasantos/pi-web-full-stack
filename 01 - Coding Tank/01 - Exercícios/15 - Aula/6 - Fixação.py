'''Enunciado
Usando o dicionário resultante do exercício 5, descubra a média de idades.'''
nomeIdade = {'Ana':25, 'Maria': 34, 'Vitória':22, 'João':32}

idades = list(nomeIdade.values())
soma = sum(idades)/len(idades)
print(soma)