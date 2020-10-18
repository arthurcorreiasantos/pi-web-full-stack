###
### Listas
###

'''
Listas são coleções de objetos em Python.
Ao invés de declarar 1 variável para cada valor que gostaríamos de armazenar,
podemos criar uma lista para armazenar vários valores.
'''

# Criando uma lista vazia.
listavazia = []

# Criando uma lista com alguns valores.
numeros = [1, 3, 7, 8, 9]

# Listas podem mesclar diferentes tipos de valores.
listamista = [14, "let's code", 0.1, True]

# Acessamos cada elemento da lista através de um índice entre colchetes.
# Os índices começam em 0.
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

# Listas são mutáveis: podemos alterar o valor de seus itens.
numeros[2] = 5
print(numeros)

# Um jeito inteligente de trabalhar com listas é utilizando loops.
indice = 0
while indice < 5:
    print(numeros[indice])
    indice = indice + 1

'''
Algumas funções podem nos ajudar a trabalhar com listas.
No exemplo acima, poderíamos usar len() caso não soubéssemos
o comprimento da lista.
'''
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice = indice + 1

# Outra função útil é lista.append()
# .append() coloca um elemento novo ao final da lista.

animais = []
resposta = 's'
while resposta == 's' or resposta == 'S':
    resposta = input('Deseja adicionar um animal à lista (s/n)? ')
    if (resposta == 's' or resposta == 'S'):
        animal = input('Digite o nome do animal: ')
        animais.append(animal) # adiciona o novo animal à lista
print(animais)

# A função lista.remove() deleta um elemento da lista.
# (mas dá erro se o elemento não existir)
animal = input('Digite o animal a ser deletado da lista: ')
animais.remove(animal)
print(animais)

# Algumas outras funções úteis:
# lista.count() conta quantas vezes um elemento aparece.
jogadores = ['Ronaldo', 'Rivaldo', 'Ronaldo', 'Adriano']
ronaldos = jogadores.count('Ronaldo')
print(jogadores)
print('Quantidade de Ronaldos: ', ronaldos)
# lista.index() busca em um elemento e fala em qual posição ele aparece.
rivaldo = jogadores.index('Rivaldo')
print("Rivaldo está na posição ", rivaldo)
# lista.sort() ordena uma lista.
jogadores.sort()
print("jogadores em ordem alfabética: ", jogadores)

# As funções max(lista) e min(lista) obtém, respectivamente, o maior e o menor valor
digitos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior = max(digitos)
menor = min(digitos)
print(digitos)
print("Maior = ", maior, "e menor = ", menor)

###
### Loops 'for'
###

'''
O for é um tipo especial de loop feito para percorrer elementos de uma coleção.
Acima vimos exemplos usando um while e um contador para percorrer uma lista.
O for elimina a necessidade de inicializarmos um contador, incrementarmos e
verificar a condição de parada.
Sintaxe:

for (variável temporária) in (lista):
    # instruções...
    # ...
O for se repete uma vez para cada elemento da lista.
A cada repetição, a variável temporária assume o valor de um elemento da lista,
na ordem da lista.
'''
fib = [1, 2, 3, 5, 8, 13]
for elemento in fib:
    print(elemento)


'''
O for pode ser usado, junto com a função range(), para gerar sequências
numéricas e contagens.
Existem 3 meios de usar o range(): especificando 1, 2 ou 3 parâmetros.
'''

# Com 1 parâmetro, ele será interpretado como valor final (exclusivo).
# O valor inicial será 0 e o incremento será 1.

for numero in range(10):
    print(numero)
    # este exemplo imprime os números de 0 a 9, de um em um

# Com 2 parâmetros, o primeiro será o valor inicial (inclusivo) e o
# segundo será o final (exclusivo).
# O incremento continuará sendo 1.

for numero in range(1,11):
    print(numero)
    # este exemplo imprime os números de 1 a 10, de um em um

# Com 3 parâmetros, o terceiro será interpretado como incremento.
for numero in range(1,20,2):
    print(numero)
    # este exemplo imprime os ímpares positivos menores do que 20
    # ele começa valendo 1 e salta de 2 em 2 até atingir ou passar 20

# O incremento pode ser também um decremento (incremento negativo).
for numero in range (10,0,-1):
    print(numero)
    #Imprimindo os números de 1 a 10 em ordem decrescente


###############
## B Ô N U S ##
###############

# É possível aninhar listas (listas de listas)

listaGrande = [ [1, 3, 5], [2, 4, 6]]
print('listaGrande[0] = ', listaGrande[0])

# Podemos usar 2 for's aninhados para percorrer listas aninhadas

for listinha in listaGrande: #seleciona uma lista interna em listaGrande
    for elemento in listinha: #seleciona cada elemento da lista interna
        print(elemento)

'''
É possível ter vários níveis de listas aninhadas: lista de lista de lista de
lista...
A regra é geral: para cada nível de lista, um for adicional será necessário
para percorrer todos os elementos.
'''
