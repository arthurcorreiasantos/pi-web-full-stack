### STRINGS ###
###############
'''
exemplo = "o Lobo ama o Bolo2"

EXEMPLO = exemplo.upper()
exemplinho = exemplo.lower()
Exemplo = exemplo.capitalize()
ExemplO = exemplo.title()
print('Upper:', EXEMPLO)
print('Lower:', exemplinho)
print('Capitalize:', Exemplo)
print('Title:', ExemplO)

exempli = exemplo.replace('o', 'i', 3)
print('Replace:', exempli)

print( exemplo[-1].isnumeric() )

preco_gasolina = 10
preco_dolar = 20
print(preco_gasolina+preco_dolar)

brasil_infos = "O preço da gasolina no Brasil é R${} e o preço do dolar é R${}".\
    format(preco_gasolina, preco_dolar)

print(brasil_infos)

print("O preço da gasolina no Brasil é R${1} e o preço do dolar é R${0}".\
    format(preco_gasolina, preco_dolar))


dia = 21
mes = 9
ano = 2020
data = '{}/{}/{}'.format(dia, mes, ano)

print(data)

print(f'{dia}/{mes:02d}/{ano}')

k = 1.38
G = 6.67
c = 2.99
pi = 3.1415926535

print(f'Constate de Boltzmann: {k} \nConstante gravitacional: {G:.1f} \nVelocidade da luz: {c:02.2f}\
    \npi: {pi:.3f}')

porcento = 0.25
print(f'{:.porcento%}')


name = "John"
age = 23
print("%s is %d years old." % (name, age))

### TUPLAS ###
##############

# Estrutura de dados => menos memoria, imutavel, função que retorna mais de uma variavel

tupla = (1, 2, 3)
tupla2 = 1,2,3


print(type(tupla))
print(tupla2[1])

#tupla2[1] = 4 NÃO FUNCIONA!!!

lista2 = list(tupla2)
print(lista2, type(lista2))'''


exemplo = "o Lobo ama o Bolo2"

lista_exemplo = exemplo.split(' ')

#string_exemplo = 'PY'.join(lista_exemplo)

print(exemplo, '\n', lista_exemplo, '\n', string_exemplo)

