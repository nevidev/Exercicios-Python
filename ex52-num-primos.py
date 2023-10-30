# ex52 - faça um programa que leia um número e diga se ele é ou não um número primo
n1 = int(input('Digite um número inteiro: '))
primo = 0
for i in range(1, n1 + 1):
    if n1 % i == 0:
        primo += 1
if primo == 2:
    print('{} é um número primo'.format(n1))
else:
    print('{} não é primo'.format(n1))