# ex60 - faça um programa que leia um número qualquer e mostre seu fatorial
from math import factorial

n1 = int(input('Digite um número inteiro para calcular seu fatorial: '))
fact = factorial(n1)
print('O fatorial de {} é {}'.format(n1, fact))

# outra maneira
n2 = int(input('Digite um número inteiro para calcular seu fatorial: '))
fact2 = 1
while n2 > 0:
    print('{}'.format(n2), end='')
    print(' x 'if n2 > 1 else ' = ', end='')
    fact2 = fact2 * n2
    n2 = n2-1
print('{}'.format(fact2))