# ex88 - faça um programa que ajude um jogador da megasena a criar palpites. O programa
# vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta
from random import randint
lista = []
sorteios = []
jogos = int(input('Quer fazer quantos jogos da MEGASENA? '))

for j in range(0, jogos):
    cont = 0
    while True:
        r = randint(1,60)
        if r not in lista:
            lista.append(r)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    sorteios.append(lista[:])
    lista.clear()
    
for i, l in enumerate(sorteios):
    print(f'Jogo {i+1}: {l}')
