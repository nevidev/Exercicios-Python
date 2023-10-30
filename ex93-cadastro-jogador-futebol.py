# ex93 - crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
# a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionário incluindo o total de gols feitos durante o campeonato

dic = {}
lista = []

dic['nome'] = input('Nome: ').strip()
total = int(input('Quantidade de partidas: '))
for v in range(0, total):
    lista.append(int(input(f'Quantos gols na partida {v+1}: ')))
dic['gols'] = lista[:]
dic['total'] = sum(lista)
print()
print(dic)
print()
for k, v in dic.items():
    print(f'{k:<5} -> {v}')
print()
print(f'O jogador {dic["nome"]} jogou {len(dic["gols"])} partidas')
for i, v in enumerate(lista):
    print(f'No jogo {i+1} fez {v} gols')
print(f'No total {dic["nome"]} fez {dic["total"]} gols')