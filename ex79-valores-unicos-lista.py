# ex79 - crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
# em uma lista. Caso o número já exista, ele não será adicionado. No final serão
# exibidos todos os valores únicos digitador em ordem crescente
lista = []

while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado\n')
    elif n in lista:
        print('Número ja existe\n')

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if cont == 'N':
        break
lista.sort()
print(f'Você digitou os valores, em ordem crescente, {lista}')