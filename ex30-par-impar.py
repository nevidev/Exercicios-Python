# ex30 - crie um programa que leia um número inteiro e mostre na tela se é par
# ou impar
n1 = int(input('Digite um número inteiro: '))
if (n1 % 2 == 0):
    print('O número {} é par'.format(n1))
else:
    print('o número {} é ímpar'.format(n1))