num = int(input('Digite um número inteiro: '))

i = 1
while i < num+1 and num % i == 0:
    i = i+1
print(i)