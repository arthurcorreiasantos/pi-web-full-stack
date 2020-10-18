### DICIONARIOS ###
###################

dicionario_linguas = {}
lista_linguas = []
tupla_linguas = ()
print(type(dicionario_linguas), type(lista_linguas), type(tupla_linguas))

lista_linguas.append('macarrão')
lista_linguas.append('penne')
lista_linguas.append('ravioli')
# tupla_linguas.append('macarrão') NÃO FUNCIONA!


### dicionario_linguas = {'pasta':'macarrão'}


dicionario_linguas['pasta'] = lista_linguas
# dicionario_linguas.update({'pasta':lista_linguas})

print(dicionario_linguas)

dicionario_linguas['pasta'] = []

lista_linguas[0] = 'penne'

print(dicionario_linguas)

dicionario_linguas = {'pasta':['macarrão', 'penne', 'ravioli'], \
    'cat':'gato', 'computer':'computador', 'mouse':'mouse', 'television':'televisão',\
        'dictionary':{'y':'e', 'hoy':'hoje', 'hola':'oi'}}

#print(dicionario_linguas['dictionary']['hoy'])
dicionario_linguas['pasta'] = 'macarrão' #adicionar item e valor ao dicionario
dicionario_linguas['who'] = 'quem'

for u in dicionario_linguas:
    print(u)

chave_linguas = list(dicionario_linguas.keys())
print(chave_linguas)
for c in chave_linguas:
    print(c)

valores_linguas = dicionario_linguas.values()
print(valores_linguas)
for v in valores_linguas:
    print(v)

itens_linguas = dicionario_linguas.items()
print(itens_linguas)

#   tupla    [tupla1, tupla2,...]
for (c,v) in itens_linguas:
    print(c)
    print(v)

print('='*40)

if 'dog' in chave_linguas:
    print(dicionario_linguas['dog'])

if 'cat' in chave_linguas:
    print(dicionario_linguas['cat'])


lista_numeros = [1,1,2,3,5,8,13,21]

if (4 in lista_numeros):
    print('4 está na lista')



nomes = ['Arthur', 'Bruno', 'Caio']
CPF = [0,1,2]

cadastro = {'Nomes':nomes, 'CPFs':CPF}
print(cadastro['Nomes'][1],cadastro['CPFs'][1]) #Como retornar índices das listas dentros dos dicionários.