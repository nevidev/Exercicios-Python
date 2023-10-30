# ex73 - crue uma tupla preenchida com os 20 primeiros colocados da tabela do 
# campeonato de futebol, na ordem de colocação. Depois mostre: apenas os 5 primeiros,
# os últimos 4 colocados, uma lista com os times em ordem alfabética, em que posição 
# está o time Cruzeiro
# tabela do dia 13/10/2023
times = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza',
'Fluminense', 'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Cuiabá', 'Internacional',
'Corinthians', 'Santos', 'Cruzeiro', 'Bahia', 'Vasco da Gama', 'Goiás', 'Coritiba',
'América-MG')

print(f'Os cinco primeiros: {times[:5]}')

print(f'Os quatro últimos: {times[-4:]}')

print(f'Ordem alfabética: {sorted(times)}')

print(f'O Cruzeiro está na posição: {times.index("Cruzeiro")+1}')