'''Enunciado
Faça uma função recursiva que apresente os números entre 1 e N, sendo N um número informado pelo usuário.'''

num = int(input('Digite um número inteiro: '))
lista = []

def subtrairum (num):
    if num >= 1:
        lista.append(num)
        num = num-1
        subtrairum(num)
subtrairum(num)
print(lista)