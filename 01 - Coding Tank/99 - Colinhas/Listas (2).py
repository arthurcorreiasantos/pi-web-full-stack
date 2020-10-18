'''numero_start = int(input('Entre com um numero de inicio:'))
numero_stop = int(input('Entre com um numero de fim:'))
numero_step = int(input('Entre com o passo/intervalo:'))


# default => padrão

# A variavel contador já está pré-declarada
# E ja vai ser incrementada automaticamente!!
for i in range(numero_start, numero_stop, numero_step):
    print(i)

# range(5) = [0, 1, 2, 3, 4]

i = 0
while i<5:
    print(i)
    i = i + 1
'''
'''
### LISTAS ###
##############

#indice   0    1        2          3
lista = [10, 10<=3, 'Nietzsche', 3.14]

print(type(lista))

print(lista[2])
print(lista[1:3])

print(lista[2:])
print(lista[-1])


numeros = [16, 32, 42, 4, 8, 15]

# ORIENTADO A OBJETOS => Dependendo do tipo da variavel, eu vou poder fazer metodos especificos

# acrescentar:

numeros.append(101212)
print('Lista com numero acrescentado:')
print(numeros)
print('='*40)

# remove:
numeros.remove(4)
print('Lista com numero removido:')
print(numeros)
print('='*40)

#colocar em ordem
numeros.sort()
print('Lista ordenada:')
print(numeros)
print('='*40)

#descobrir a posição com base no elemento
print('O elemento', 101212, 'tem como indice', numeros.index(101212))
print('='*40)

# comprimento
print('O tamanho da minha lista é', len(numeros))
print('='*40)




# condições: quais são pares, etc
print('Lista percorrida com while:')
i = 0
while i < len(numeros):
    print(numeros[i])
    i = i + 1
print('='*40)




# range(len(lista)) = range(6) = [0, 1, 2, 3, 4, 5]

numeros_2 = [0, 1000, -500, 7, 219, 3]

print('Lista percorrida com indice do for:')
for i in range(len(numeros)):
    print(numeros[i] + numeros_2[i])
print('='*40)

print('Lista percorrida com for:')

# range(6)=  [0   1   2   3   4     5]
# numeros = [8, 15, 16, 32, 42, 101212]

for elemento in numeros:
    if elemento%2==0:
        print(elemento)
print('='*40)


floresta = ['arvore', 'rio', 'onça', 'urso']
for camaleao in floresta:
    print(camaleao)
print('='*40)


# maximo, minimo

print(max(numeros))
print(min(numeros))

numeros.reverse()

print(numeros)

'''

### Matrizes
'''
| a b c|
| d e f|
'''

listinha1 = ['elemento X', 'elemento agua', 'elemento Carbono']
listinha2 = [67, 13, 45]
listinha3 = [6.67, 2.28, 1.38]

listona = [listinha1, listinha2, listinha3]

#print(listona.index())

# SyntaxError: pontuação (''', (), ;), etc
# TypeError: operações entre tipos diferentes, metodo improprio para o tipo, etc
# ValueError: valor não encontrado (esquecemos de definir uma variavel, etc)
# AttributeError: errei o atributo da variavel (a função que tentamos puxar)
# IndexError: lista acabou os elemetos! indice fora do range

print(listona[1][1])
print(listinha2[1])


for listinha in listona:
    for elemento_individual in listinha:
        print(elemento_individual)



listinha1 = ['elemento X', 'elemento agua', 'elemento Carbono', 'elemento fogo']
listinha2 = [67, 13, 45, 4, 41]
listinha3 = [6.67, 2.28, 1.38]

listona = [listinha1, listinha2, listinha3]


for i in range(len(listona)): # percorrer os indices de listona
    for j in range(len(listona[i])): # percorrer os indices de listinha1, listinha2, listinha3
        print(listona[i][j]) # o elemento com indices i, j

# elemento com indice 0,0: elemento X
# elemento com indice 2,3: NÃO EXISTE
# elemento com indice 2,1: 2.28

for i in listona:
    for x in i:
        print(x)