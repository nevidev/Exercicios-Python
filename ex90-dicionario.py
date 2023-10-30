# ex90 - faça um programa que leia nome e média de um aluno, guardando também a 
# situação em um dicionário. No final mostre o conteúdo da estrutura na tela

dic = {}
lista = []
dic['nome'] = input('Nome: ').strip()
dic['media'] = int(input('Média: '))

if dic['media'] < 6:
    dic['sit'] = 'Reprovado'
else:
    dic['sit'] = 'Aprovado'
lista.append(dic.copy())

print(f'Aluno: {lista[0]["nome"]}')
print(f'Nota média: {lista[0]["media"]}')
print(f'Situação: {lista[0]["sit"]}')

print(lista)
