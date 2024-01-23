# ex76 - crie um programa que tenha uma tupla unica com nomes de produtos e seus
# preços. No final mostre uma listagem de preços organizando os dados em forma tabular

prod = ('Arroz', 15, 'Feijão', 12, 'Frango', 10, 'Batata', 6)
print('-'*30)
print(f'{"PREÇOS":^30}')
for p in range(0, len(prod)):
    if p % 2 == 0:
        print(f' {prod[p]:.<20}', end='')
    else:
        print(f'R$ {prod[p]:>1.2f}')
print('-'*30)