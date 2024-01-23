# ex98 - faça um programa que tenha uma função chamada contador(), que receba
# três paraâmetros: início, fim e passo e realize a contagem
# seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def contador(inicio, fim, passo):
    while passo == 0:
        passo = int(input('Passo 0 não é possível. Tente outro valor: '))
    if passo < 0:
        passo = passo * -1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim: 
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.1)
            cont += passo
        print('\n')
    
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.1)
            cont -= passo
        print('\n')
   
# main
contador(1, 10, 1)
contador(10, 0, 2)

print('Personalize sua contagem: ')
inicio = int(input('Primeiro número: '))
fim = int(input('Ultimo número: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
