# ex99 - faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros
# seu programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep
def maior(* nums):
    cont = 0
    maior = 0
    print()
    print('Valores:', end=' ')
    for n in nums:
        sleep(0.3)
        print(f'{n}', end=' ', flush=True)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'\nForam informados {cont} valores')
    print(f'O maior valor foi {maior}')

# main    
maior(2, 9, 4, 5, 6)
maior(3, 4, 1)
maior()
