# ex54 - crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores
from datetime import date
dataHoje = date.today()
hoje = dataHoje.strftime('%Y')
maiores = 0
menores = 0
# idade = int(hoje) - nasc
for i in range(0,7):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = int(hoje) - nasc
    if idade < 19:
        menores += 1
    else:
        maiores += 1
print('Existem {} maiores de idade e {} menores de idade'.format(maiores, menores))