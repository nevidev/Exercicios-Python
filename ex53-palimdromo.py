# ex53 - crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
# desconsiderando os espaços
frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''

for i in range(len(juntar) - 1, -1, -1):
    inverso = inverso + juntar[i]
print('O inverso de {} é {}'.format(juntar, inverso))
if inverso == juntar:
    print('A frase digitada é igual a ela mesma de trás pra frente, é palíndromo')
else:
    print('Não é palíndromo')