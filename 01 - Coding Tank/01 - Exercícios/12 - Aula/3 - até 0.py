lista = []
num = int(input('Digite um número inteiro: '))
while num != 0:
    lista.append(num)
    num = int(input('Digite outro número inteiro: '))
print('Você digitou', len(lista), 'números')