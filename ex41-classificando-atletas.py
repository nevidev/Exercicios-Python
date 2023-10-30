# ex41 - a confederação nacional de natação precisa de um programa que leia o ano de 
# nascimento de um atleta e mostre sua categoria, de acordo com a idade
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 20 anos: senior
# acima: master
from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
dataHoje = date.today()
hoje = dataHoje.strftime('%Y')
idade = int(hoje) - nasc
if idade <= 9:
    print('Com idade de {} anos, é um atleta mirim'.format(idade))
elif idade > 9 and idade <= 14:
    print('Com idade de {} anos, é um atleta infantil'.format(idade))
elif idade > 14 and idade <= 19:
    print('Com idade de {} anos, é um atleta junior'.format(idade))
elif idade == 20:
    print('Com idade de {} anos, é um atleta sênior'.format(idade))
else:
    print('Com idade de {} anos, é um atleta master'.format(idade))