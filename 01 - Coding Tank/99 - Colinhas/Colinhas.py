###
### Introdução: variáveis, entradas e saídas
###


# Linhas iniciadas com # são comentários.
# Comentários são ignorados pelo Python e servem para explicar o código.

"""
O símbolo # é um comentário de apenas 1 linha.
Usando 3 aspas simples consecutivas é possível abrir um bloco de comentário
de múltiplas linhas. O bloco se encerra com outras 3 aspas simples.
"""

'''
Variáveis são pedacinhos de memória onde guardamos dados.
Sempre que referenciamos o nome de uma variável, o dado é acessado.
Criamos variáveis dando um nome a elas e usando o sinal de igual (=)
para atribuir um valor.
'''
x = -10 # uma variável do tipo inteiro (int)
y = 3.14 # uma variável do tipo real (float)
escola = "Let's Code" # uma variável texto (string)
primeiraAula = True # uma variável lógica (booleana)

'''
Note que o operador igual (=) NÃO possui o mesmo comportamento
da matemática.
Na matemática, ele é um operador bidirecional:
x = 2y seria a mesma coisa que 2y = x.
No Python, ele é o que chamamos de um operador de ATRIBUIÇÃO:
A expressão à direita do sinal é resolvida e seu resultado é armazenado
na variável à esquerda.
'''

# Podemos exibir textos na tela e/ou valores de variáveis com a função print().
print('eu estudo na ', escola)
print('pi vale', y)

# Podemos ler valores do teclado com a função input().
# Ela permite que a gente passe uma mensagem para o usuário.
nome = input('Digite o seu nome: ')

# Tudo que é lido por input() é considerado uma string (str).
# Para tratar como outros tipos de dados é necessário converter:
peso = float(input('Digite o seu peso: ')) # lê o peso como número real
idade = int(input('Digite a sua idade: ')) # lê a idade como número inteiro

print(nome, 'pesa', peso, 'kg e tem', idade, 'anos de idade')

# Podemos fazer operações aritmeticas simples
a = 2 + 3  # Soma
b = 2 - 3  # Subtração
c = 2 * 3  # Multiplicação
d = 2 / 3  # Divisão
e = 2 // 3 # Divisão inteira
f = 2 ** 3 # Potência
g = 2 % 3  # Resto de divisão

print (a, b, c, d, e, f, g)

# Podemos fazer operações dentro do print

print (a+1, b+1)

#Podemos fazer operações com variáveis não inteiras
nome = input('Digite seu primeiro nome:')
nome = nome + ' Schmitt'
print(nome)

booleana = True
booleana = booleana - 1
print(booleana)

#Podemos imprimir valores com o número de casas decimais que queremos
val = 3.141592653589
print('O número pi com 3 casas decimais vale {:06.3f}'.format(val))


###
### Estruturas condicionais: if, elif e else
###

'''
O if testa uma condição:
- se ela for verdadeira, seu conteúdo é executado;
- caso contrário, seu conteúdo é ignorado.
'''

idade = int(input('Digite sua idade:'))
if idade >= 12:
    print('Você pode entrar na montanha russa.')
print('Obrigado por participar.')

altura = float(input('Digite sua altura, em metros:'))
if idade >= 12 and altura >= 1.60:
    print('Você pode entrar na montanha russa.')
print('Obrigado por participar.')

'''
Utilizamos um 'tab' antes de cada linha pertencente ao if.
No exemplo acima, a linha 'obrigado por participar' sempre será exibida.
Já a linha 'Você pode entrar na montanha russa.' só será exibida se a idade digitada for maior ou igual a 12 e a altura digitada for maior ou igual a 1.60.
'''
'''
Além do >=, temos o operador lógico que testa igualdade, ==, e o menor, <.
Quanto a conectores, temos além do "and" os conectores "or" e "and"
'''
'''
Em alguns casos, queremos que o programa escolha entre 2 casos
mutuamente exclusivos.
Para isso utilizamos o else.
O else não possui condição para verificar.
O else sempre vem imediatamente após um if e é executado se o if for ignorado.
'''

idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura, em metros:'))
if idade >= 12 and altura >= 1.60:
    print('Você pode entrar na montanha russa.')
else:
    print('Você não pode entrar na montanha russa.')
print('Obrigado por participar.')


# É possível "aninhar" diversos if's e else's.
# O programa abaixo só deixa a pessoa entrar no brinquedo se tiver idade e altura mínimas:
idade = int(input('Digite sua idade:'))
if idade >= 12:
    resposta = input('Você gostaria de entrar nesta montanha russa?')
    if (resposta == 'sim'):
        print('Por favor, entre!')
    else:
        print('Ok então')
else:
    print('Você não tem idade para esse brinquedo.')
'''
Podemos testar diversos casos mutuamente exclusivos utilizando o 'elif'.

elif é a contração de "else if" - ou seja, caso um if não seja executado,
você pode propor uma nova condição para ser testada.
'''

exercicios = int(input('Quantos exercícios de Python vc já fez?'))

if exercicios > 30:
    print('Já está ficando profissional!')
elif exercicios > 20:
    print('Tá indo bem, bora fazer mais alguns!')
elif exercicios > 10:
    print('Vamos tirar o atraso?')
else:
    print('Xiiii...')

'''
Podemos encadear condições usando os operadores 'and' e 'or':
- o 'and' exige que todas as condições sejam verdadeiras;
- o 'or' exige que uma condição seja verdadeira.
'''

numero1 = int(input('Digite um número maior do que 0 E menor do que 10:'))
if numero1 > 0 and numero1 < 10:
    print('Muito bem!')
else:
    print('Teimoso!')

numero2 = int(input('Digite um número menor do que 0 OU maior do que 10:'))
if numero2 < 0 or numero2 > 10:
    print('Aí sim!')
else:
    print('Mas poxa vida...')

###
### Malha de repetição (loop) - While
###

'''
O while é bastante parecido com um 'if': ele possui uma expressão,
e é executado caso ela seja verdadeira.

Mas o if é executado apenas uma vez e depois o código segue adiante.
O while não: ao final de sua execução, ele torna a testar a expressão,
e caso ela seja verdadeira, ele repete sua execução.
'''

'''
Uma utilidade interessante do while é obrigar o usuário a
digitar apenas entradas válidas.
'''

# o exemplo abaixo não aceita um salário menor do que o mínimo atual:
salario = 0.0
while salario < 998.0:
    salario = float(input('Digite o seu salário: '))
print('Você ganha ', salario)

'''
Todo tipo de código que deve se repetir várias vezes pode ser feito
com o while, como somar vários valores, gerar uma sequência etc.
Nestes casos, é normal utilizar um contador:
'''
numero = int(input('Digite quantas provas você fez: '))
contador = 1
soma = 0
while contador <= numero:
    nota = float(input('Digite a nota da prova ' + str(contador) + ':'))
    soma = soma + nota
    contador = contador + 1
media = soma/numero
print('Você fechou com média:', media)

'''
Um jeito de forçar um loop a ser interrompido é utilizando o comando 'break'.
O loop abaixo em tese seria infinito, mas se a condição do if for verificada,
o break é executado e conseguimos escapar do loop:
'''
while True:
    resposta = input('Digite SAIR para sair: ')
    if resposta == 'SAIR':
        break
    else:
        print('E lá vamos nós de novo...')

