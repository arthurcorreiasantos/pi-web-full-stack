'''Faça uma função que receba uma lista com uma quantidade indeterminada de números 
e informe quantos números sem repetição existem na lista.

Exemplo
input: [1,2,3,3,4,5]
output: 4 números sem repetição'''

'''

Opção 1:

Se eu tenho 6 números e um que repete 2 vezes, logo, eu vou ter 4 números que não se repetem.

Então eu posso só subtrair a soma dos números com contagem >=2 e subtrair do tamanho total da lista.

Opção 2:

Posso percorrer cada valor e verificar se ele aparece mais de uma vez e quantas vezes ele aparece./
Tipo, a primeira posição vai comparando com cada posição e então, cada vez que for igual ao valor da posição
o contador soma. O número mínimo vai ser 1 e toda vez o que equivale a zero repetições.

Então os contadores de cada número em um dicionário e conseguir uma forma de contar
quantos zeros tem no dicionário.



'''

def contarvalores ()

    num = [1, 2, 2, 4, 5, 3, 9, 2, 3, 5, 3, 7]
    soma = 0

    for i in range(len(num)):
        if num.count(num[i]) == 1:
            soma = soma + num.count(num[i])
    print(soma,' números sem repetição.')

contarvalores()