# ex86 - crie um programa que crie uma matriz 3x3 e preencha com valores lidos
# pelo teclado. No final mostre a matriz na tela, com formatação correta

lista = [[], [], []]

for v1 in range(0,3):
    n1 = int(input(f'Digite o {v1+1}º valor da 1ª linha: '))
    lista[0].append(n1)
for v2 in range(0,3):
    n2 = int(input(f'Digite o {v2+1}º valor da 2ª linha: '))
    lista[1].append(n2)
for v3 in range(0,3):
    n3 = int(input(f'Digite o {v3+1}º valor da 3ª linha: '))
    lista[2].append(n3)
    
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')