# ex82 - crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso crie duas listas extras que vão conter apenas os valores pares e ímpares
# digitados, ao final mostre as três listas

lista = []
par = []
impar = []

while True:
    n1 = lista.append(int(input('Digite um número: ')))
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer adicionar mais valores? S/N ').strip().upper()[0]
    if cont == 'N':
        break

for n in lista:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)

print(f'Lista: {lista}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')