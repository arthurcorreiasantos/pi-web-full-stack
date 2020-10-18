lista = []
maiores = []
soma = 0
media = 0.0

for i in range(10):
    num = int(input('Digite um número: '))
    lista.append(num)
    soma = soma + num

num_elementos = len(lista)
media = soma / num_elementos

for i in range(10):
    if lista[i] > media:
        maiores.append(lista[i])
print('A média dos números é: ', media)
print('Os números', maiores, 'são maiores que a média')