'''Enunciado
Faça um programa que leia 10 números do usuário e os coloque corretamente no dicionário D abaixo.

D = {'pares': [], 'impares':[]}'''

D = {'pares':[], 'impares':[]}
pares = []
impares = []

for i in range(10):
    num = int(input('Digite um número inteiro: '))
    if num%2 == 0:
        pares.append(num)
    else:
        impares.append(num)
D.update({'pares':pares, 'impares':impares})
print(D['pares'])
print(D['impares'])