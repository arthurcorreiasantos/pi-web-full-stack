traducao = {'if':'se', 'while':'enquanto','>':'maior que','<':'menor que','>=':'maior igual que','<=':'menor igual que','==':'igual a', \
'!=':'diferente de','print':'imprima o valor da variável'}
traduzido = []

py = str(input('Digite o código em python: '))
py = py.split()

for i in range(len(py)):
    if py[i] in traducao:
        traduzido.append(traducao[py[i]])
    else:
        traduzido.append(py[i])
    
print(' '.join(traduzido))