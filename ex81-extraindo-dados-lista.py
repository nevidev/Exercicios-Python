# ex81 - crie um programa que vai ler vários números e colocar em uma lista
# depois, mostre: quantos números foram digitados, a lista decrescente, se o valor
# 5 foi digitado nessa lista
lista = []
quantidade = 0

while True:
    lista.append(int(input('Digite um número: ')))
    quantidade += 1
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer adicionar mais valores? S/N ').strip().upper()
    if cont == 'N':
        break

print(f'Foram digitados {quantidade} números')
lista.sort(reverse=True)
print(f'Lista decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)+1}')
else:
    print('O valor 5 não foi digitado')
