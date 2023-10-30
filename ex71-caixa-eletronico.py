# crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
# pergunte ao usuário qual será o valor a ser sacado (inteiro) e o programa vai 
# informar quantas cédulas de cada valor serão entregues
# considerar cédulas de 50, 20, 10 e 1 real
n = int(input('Digite um valor inteiro para saque: R$ '))
while True:
    cinq = n // 50
    vinte = (n - cinq*50) // 20
    dez = (n - vinte*20 - cinq*50) // 10
    um = (n - dez*10 - vinte*20 - cinq*50) // 1

    if n >= 50:
        if cinq > 1:
            print(f'{cinq} notas de R$ 50')
        elif cinq == 1:
            print(f'{cinq} nota de R$ 50')
    if n >= 20:
        if vinte > 1:
            print(f'{vinte} notas de R$ 20')
        elif vinte == 1:
            print(f'{vinte} nota de R$ 20')
    if n >= 10:
        if dez > 1:
            print(f'{dez} notas de R$ 10')
        elif dez == 1:
            print(f'{dez} nota de R$ 10')
    if n >= 1:
        if um > 1:
            print(f'{um} notas de R$ 1')
        elif um == 1:
            print(f'{um} nota de R$ 1')
    break