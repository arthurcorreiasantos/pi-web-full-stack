def saudacoes (nome, horario):
    periodo = {horario < 12:'Bom dia, ', horario >= 12 and horario < 18:'Boa tarde, ', horario > 18:'Boa noite, '}
    return periodo[True] + nome


nome = str(input('Digite o seu nome: '))
horario = int(input('Digite o número referente a hora do dia: '))
print(saudacoes(nome, horario))