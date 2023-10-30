# ex72 - crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
# extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado(entre
# 0 e 20) e mostrá-lo por extenso

num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', \
'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', \
'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    num1 = int(input('Digite um valor entre 0 e 20: '))
    if num1 > 20 or num1 < 0:
        print('Escolha números entre 0 e 20\n')
    else:
        print(f'número: {num[num1]}')
