# ex94 - crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No
# final mostre: quantas pessoas foram cadastradas, a média de idade do grupo, uma
# lista com todas as mulheres, uma lista com todas as pessoas com idade acima da
# média
dic = {}
lista = []
soma = 0
while True:
    dic['nome'] = input('Digite o nome: ').strip()
    while True:
        dic['sexo'] = input('Digite o sexo (M/F): ').strip().upper()[0]
        if dic['sexo'] in 'MF':
            break
        print('Digite apenas M ou F')
    dic['idade'] = int(input('Digite a idade: '))
    soma += dic['idade']
    lista.append(dic.copy())
    while True:
        resp = input('Quer adicionar mais? (S/N): ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Digite apenas S ou N')
    if resp == 'N':
        break
print()
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'Média das idades: {soma/len(lista):.2f}')

print(f'Mulheres cadastradas: ', end='')
for v in lista:
    if v['sexo'] == 'F':
        print(f'{v["nome"]}; ', end='')
print()
print(f'Pessoas com idade acima da média: ')
for v in lista:
    if v['idade'] > soma/len(lista):
        for k, v in v.items():
            print(f'{k} -> {v}; ', end='')