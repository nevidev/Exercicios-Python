# ex25 - crie um programa que leia o nome de uma pessoa e diga se ela tem
# "SILVA" no nome
nome = input('Digite seu nome: ').strip()
maiu = nome.upper()
sobrenome = ('SILVA' in maiu)
if (sobrenome == True):
    print('O nome contem Silva')
else:
    print('Não tem Silva no nome')