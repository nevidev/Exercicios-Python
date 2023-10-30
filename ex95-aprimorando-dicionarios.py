# ex95 - aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador
jogadores = []
dic = {}
lista = []
while True:
    dic.clear()
    dic['nome'] = input('Nome: ').strip()
    total = int(input('Quantidade de partidas: '))
    lista.clear()
    for v in range(0, total):
        lista.append(int(input(f'Quantos gols na partida {v+1}: ')))
    dic['gols'] = lista[:]
    dic['total'] = sum(lista)
    jogadores.append(dic.copy())
    while True:
        resp = input('Quer adicionar mais jogador? (S/N): ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Digite apenas S ou N')
    if resp == 'N':
        break
print()
print('num  ', end='')
for i in dic.keys():
    print(f'{i:<15}', end='')
print()
for i, v in enumerate(jogadores):
    print(f'{i:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    busca = int(input('Digite o num do jogador para ver os dados dele (999 para parar): '))
    if busca == 999:
        print('Encerrado')
        break
    if busca >= len(jogadores):
        print(f'Erro, jogador com num {busca} inexistente')
    else:
        print(f' Jogador {jogadores[busca]["nome"]}: ')
        for i, v in enumerate(jogadores[busca]['gols']):
            print(f' Jogo {i+1} fez {v} gols')
print()