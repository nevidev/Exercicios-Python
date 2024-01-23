# ex89 - crie um programa que leia nome e duas notas de vários alunos e guarde tudo
# em uma lista composta. No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente
lista = []

while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])

    cont = ' '
    while cont not in 'SN':
        cont = input('Quer adicionar mais alguém? (S/N): ').strip().upper()[0]
    if cont == 'N':
        break
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')

for i, a in enumerate(lista):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.2f}')

while True:
    perg = int(input('Digite o nº do aluno que quer consultar: '))
    if perg == 999:
        break
    if perg <= len(lista):
        print(f'Aluno: {lista[perg-1][0]}, notas: {lista[perg-1][1]}')
