# ex96 - faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular(largura e comprimento) e mostre a área
# do terreno
def area(l, c):
    print(f'A área do terreno é de {l * c}m² ')

larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
