### FUNÇÕES ###
###############
'''
def resposta_vida():
    print('A resposta da vida, do universo e de tudo mais é 42')

lista = [2, 4, 6, 8]
dicionario = {'batata':4, 'feijão':10, 'ovo':1}
corda = 'string'

resposta_vida()
lista.append(12)
print(lista)
resposta_vida()
st_ing = corda.split('r')
print(st_ing)
resposta_vida()
'''
###### Por que None? print(resposta_vida())
'''
def fun_print_dicionario(bobesponja, chave, valor):
    bobesponja[chave] = valor
    print(bobesponja)


dici = {}
while True:
    chave = input('Entre com a chave para o dicionario: ')
    valor = input('Entre com o valor para o dicionario: ')
    
    if chave == '0':
        break

    fun_print_dicionario(dici, chave, valor)

print(bobesponja)
'''
'''
def funcionarios(a, b, c, d, e):
    print('Meus funcionarios são:', a, 'e', b, 'e',c, 'e', d, 'e', e)

a = 'Mario'
x = 'Maria'
y = 'Cão'
funcionarios(a , x, 'Pão', y, 'José' )
'''
'''
def par(numero):
    if numero%2==0:
        return 'Verdadeiro'
    else:
        return False

num = 10
print('O numero', num, 'é par?', type(par(num)))

num = 7
sete_par = par(num)
print(sete_par)

num = 9
nove_par =  par(num)
if nove_par==True:
    print('Nove é par')
'''

### RECURSIVIDADE OU FUNÇÕES RECURSIVAS

def funcao_recursiva(numero):
    print(numero) #10 \n 10 \n 10 ....
    funcao_recursiva(numero)

def funcao_recursiva_2(numero):
    print(numero) # 10 \n 9 \n 9
    funcao_recursiva(numero-1)

def funcaoRecursiva(numero):
    if (numero != 1):
        funcaoRecursiva(numero - 1)
    print(numero)


print("Testando a função recursiva:")
funcaoRecursiva(3)


'''
numero = 10
if (numero != 1):
    funcao_generica(numero - 1)
print(numero)'''