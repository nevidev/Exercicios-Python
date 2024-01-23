# ex87 - aprimore o desafio anterior, mostrando no final: A soma de todos os valores
# pares digitados, a soma dos valores da 3ª coluna, o maior valor da segunda linha

lista = [[], [], []]
par = []

for v1 in range(0,3):
    n1 = int(input(f'Digite o {v1+1}º valor da 1ª linha: '))
    lista[0].append(n1)
    if n1 % 2 == 0:
        par.append(n1)
for v2 in range(0,3):
    n2 = int(input(f'Digite o {v2+1}º valor da 2ª linha: '))
    lista[1].append(n2)
    if n2 % 2 == 0:
        par.append(n2)
for v3 in range(0,3):
    n3 = int(input(f'Digite o {v3+1}º valor da 3ª linha: '))
    lista[2].append(n3)
    if n3 % 2 == 0:
        par.append(n3)
    
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')
print(f'Valores pares somandos: {sum(par)}')
print(f'Valores da 3ª coluna somados: {sum([lista[0][-1], lista[1][-1], lista[2][-1]])}')
print(f'Maior valor da 2ª linha: {max(lista[1])}')
