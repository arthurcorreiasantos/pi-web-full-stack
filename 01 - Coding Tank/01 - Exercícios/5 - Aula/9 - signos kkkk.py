dia = int(input('Qual o dia do seu nascimento? '))
mes = input('Qual o mês do seu nascimento? "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"')
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
#num_mes = meses.index(mes)
dias = range(1,31)

'''Signo	Intervalo
Áries	21 março a 20 abril
Touro	21 abril a 20 maio
Gêmeos	21 maio a 20 junho
Câncer	21 junho a 22 julho
Leão	23 julho a 22 agosto
Virgem	23 agosto a 22 setembro
Libra	23 setembro a 22 outubro
Escorpião	23 outubro a 21 novembro
Sagitário	22 novembro a 21 dezembro
Capricórnio	22 dezembro a 20 janeiro
Aquário	21 janeiro a 18 fevereiro
Peixes	19 fevereiro a 20 março
'''

if (dia >= 21 and mes == 'Março') and (dia <= 20 and mes == 'Abril'):
    print('O Signo é Áries')
elif (dia >= 21 and mes == 'Abril') and (dia <= 20 and mes == 'Maio'):
    print('O Signo é Touru')