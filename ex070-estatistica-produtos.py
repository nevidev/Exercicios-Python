# ex70 - crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar. No final mostre: qual o total gasto
# na compra, quantos produtos custam mais de R$ 1000, qual é o nome do produto
# mais barato
preco1k = 0
total = 0
menorValor = 0
contador = 0
produtoBarato = ''
while True:
    nome = input('Qual o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: '))
    if preco > 1000:
        preco1k += 1
    total = total + preco
    contador += 1
    if contador == 1:
        menorValor = preco
        produtoBarato = nome
    else:
        if preco < menorValor:
            menorValor = preco
            produtoBarato = nome
    perg = ' '
    while perg not in 'SN':
        perg = input('Quer adicionar mais produto? (S/N) ').strip().upper()[0]
    if perg == 'N':
        break
print(f'Total gasto R$ {total:.2f}')
print(f'Produtos acima de R$ 1000: {preco1k}')
print(f'Produto mais barato: {produtoBarato}, custando R$ {menorValor:.2f}')
