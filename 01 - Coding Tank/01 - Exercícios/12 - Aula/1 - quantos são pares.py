lista = []
pares = []

for i in range(10):
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
print('Os números pares são: ', pares)