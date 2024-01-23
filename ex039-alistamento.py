# ex39 - faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
# com sua idade: 
# se ele ainda vai se alistar;
# se é a hora de se alistar;
# se ja passou o tempo de alistamento;
# seu programa também deverá mostrar o tempo que falta ou o prazo que passou
from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
dataHoje = date.today()
hoje = dataHoje.strftime('%Y')
idade = int(hoje) - nasc
if idade == 17:
    print('Ainda falta {} ano para se alistar'.format(18 - idade))
elif idade < 17:
    print('Ainda faltam {} anos para se alistar'.format(18 - idade))
elif idade == 18:
    print('É hora de se alistar')
elif idade == 19:
    print('Ja passou do tempo de se alistar em {} ano'.format(idade - 18))
else:
    print('Ja passou do tempo de se alistar em {} anos'.format(idade - 18))