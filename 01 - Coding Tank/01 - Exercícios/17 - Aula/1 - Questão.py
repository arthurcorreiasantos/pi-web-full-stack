num = int(input('Digite um número inteiro entre 1 e 100: '))

import random
num_sorteado = random.randint(1, 100)

while num != num_sorteado:
    if num > num_sorteado:
        print('Chute muito alto')
        num = int(input('Digite outro número inteiro entre 1 e 100: '))
    elif num < num_sorteado:
        print('Chute muito baixo')
        num = int(input('Digite outro número inteiro entre 1 e 100: '))

print('Você acertou! O número é', num_sorteado)