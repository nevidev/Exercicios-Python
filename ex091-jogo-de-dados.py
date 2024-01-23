# ex91 - crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final coloque esse dicionário em
# ordem, sabendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep
from operator import itemgetter

dic = {'jogador1':randint(1,6), 
       'jogador2':randint(1,6),
       'jogador3':randint(1,6),
       'jogador4':randint(1,6)}
lista = []

for i, v in dic.items():
    print(f'{i} tirou o número {v}')
    sleep(0.5)
print('           RANKING')
lista = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(lista):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos')