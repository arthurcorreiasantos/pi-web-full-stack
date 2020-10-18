'''Enunciado
Faça uma função recursiva que retorne o fatorial de um número informado pelo usuário.
O fatorial de um número N (N!) é a multiplicação dos números entre 1 e N. Quando N = 0, N! = 1.'''

'''Fatorial de 3 é 3*2*1 = 6
Fatorial de 4 é 4*3*2*1 = 24'''

'''O que eu posso fazer?

O script recebe o número N e então armazena esse N
Então subtrai esse N de 1 e multiplica pelo número armazenado

Ouuu
Posso pegar o 1, multiplicar ele mais o próximo
'''

n = 3
c = 1
i = 0
def f (i, c):
    while i != n:
        i = i + 1
        c = (c+1) * i
        f (i,c)
f(i, c)
print(c)