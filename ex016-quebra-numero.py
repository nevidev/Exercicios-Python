# ex16 - crie um programa que leia um numero real qualquer pelo teclado
# e mostre na tela a sua porção inteira
from math import floor, ceil
n1 = float(input('Digite um número: '))
print('Arredondando para baixo teríamos: {}'.format(floor(n1)))
print('Arredondando para cima teríamos: {}'.format(ceil(n1)))
print('Arredondando com exclusão de casas decimais: {:.0f}'.format(n1))