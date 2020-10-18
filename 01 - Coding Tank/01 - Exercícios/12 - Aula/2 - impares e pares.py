lista = []
pares = []
impares = []
for i in range(10):
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)
print('Os números pares são: ', pares)
print('Os números impares são: ', impares)