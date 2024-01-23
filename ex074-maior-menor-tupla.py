# ex74 - crie um programa que vai gerar cinco números aleatórios e colocar em uma
# tupla. Depois disso mostre a listagem de números gerados e também indique o menor 
# e maior número em questão na tupla
from random import randint

numeros = randint(0, 10), randint(0, 10), randint(0, 10), \
randint(0, 10), randint(0, 10)

print(f'Os números são: {numeros}')
print('Os números são: ', end='')

for r in numeros:
    print(f'{r}', end=' ')
print(f'\nMaior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')

