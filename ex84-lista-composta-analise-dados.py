# ex84 - faça um programa que leia nome e peso de varias pessoas guardando em uma
# lista. Mostre: quantas pessoas foram cadastradas, uma listagem com as pessoas
# mais pesadas, uma listagem com as pessoas mais leves
# 100k+ -> pesada, 60kg- -> leve
dados = []
lista = []
pesado = 0
leve = 0

while True:
    dados.append(str(input('Nome: ').strip()))
    dados.append(float(input('Peso em Kg: ')))
    if len(lista) == 0:
        pesado = dados[1]
        leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    lista.append(dados[:])
    dados.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer adicionar mais alguém? (S/N): ')).strip().upper()[0]
    if cont == 'N':
        break

print(f'{len(lista)} pessoas cadastradas')
print(f'Maior peso foi de {pesado}Kg ->', end=' ')
for p in lista:
    if p[1] == pesado:
        print(f'"{p[0]}"', end=' ')
print(f'\nMenor peso foi de {leve}Kg ->', end=' ')
for p in lista:
    if p[1] == leve:
        print(f'"{p[0]}"', end=' ')
