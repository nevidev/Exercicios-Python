# ex92 - crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de
# ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e 
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar
# aposentadoria com 35 anos, para exemplo
from datetime import date

dic = {}
hoje = date.today()
ano = hoje.year

dic['nome'] = str(input('Digite o nome: ')).strip()
dic['nasc'] = int(input('Ano de nascimento: '))
dic['cart'] = int(input('Carteira de trabalho (0 não tem): '))
dic['idade'] = ano - dic['nasc']
if dic['cart'] != 0:
    dic['contrat'] = int(input('Qual o ano de contratação? '))
    dic['sal'] = float(input('Qual o salário? R$ '))
else:
    dic['contrat'] = ano
dic['aposentadoria'] = (35 - (ano - dic['contrat'])) + dic['idade']

print('-'*15)
for i, v in dic.items():
    print(f'{i}: {v}')
print()
