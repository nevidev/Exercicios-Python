# ex100 - faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
# os valores PARES sorteador pela função anterior
from random import randint
from time import sleep
lista = []
def sorteia():
    cont = 0
    print(f'Os números sorteados foram: ', end='')
    while cont < 5:
        s = randint(1,10)
        lista.append(s)
        cont += 1
        sleep(0.3)
        print(f'{s}', end=' ', flush=True)
    
def somaPar():
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma = soma + i
    print(f'\nA soma dos pares deu: {soma}')
        
# main
sorteia()
somaPar()