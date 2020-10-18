cpfs = []
nomes = []
emails= []
base = {}
lista = ()

num = str(input('Digite o número referente a opção: 1 - Cadastrar, 2 - Visualizar os cadastrados e 3 - Buscar um cadastro específico. Digite 4 se quiser sair do programa: '))

while num != '4':
    #menu principal. adicionando nomes a lista e dicionário
    if num == '1':
        cpf = str(input('Digite o CPF: '))
        nome = str(input('Digite o nome: '))
        email = str(input('Digite o e-mail: '))
        cpfs.append(cpf)
        nomes.append(nome)
        emails.append(email)
        base = {'CPF':cpfs,'Nome':nomes, 'e-mail': emails}
        print('Usuário cadastrado')
        num = str(input('Digite o número referente a opção: 1 - Cadastrar, 2 - Visualizar os cadastrados e 3 - Buscar um cadastro específico. Digite 4 se quiser sair do programa: '))
    elif num == '2':
        #Imprimir base
        for i in range(len(cpfs)):
            print('Nome: ',nomes[i],' ,e-mail: ',emails[i],' ,CPF: ',cpfs[i])
            
        
        num = str(input('Digite o número referente a opção: 1 - Cadastrar, 2 - Visualizar os cadastrados e 3 - Buscar um cadastro específico. Digite 4 se quiser sair do programa: '))        
    elif num == '3':
        #buscar um cadastro pelo CPF
        cpf = str(input('Digite o CPF: '))
        posicao = cpfs.index(cpf)
        print('O usuário do CPF ', cpf, ' é o ',(base['Nome'][posicao]), 'email: ',(base['e-mail'][posicao]))
        num = str(input('Digite o número referente a opção: 1 - Cadastrar, 2 - Visualizar os cadastrados e 3 - Buscar um cadastro específico. Digite 4 se quiser sair do programa: '))