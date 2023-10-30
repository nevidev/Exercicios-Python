# ex85 - crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separado os valores pares e impares.
# No final mostre os valores pares e impares em ordem crescente

lista = [[], []]

for v in range(0,7):
    n = int(input(f'Digite o {v+1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(f'Lista completa: {lista}')
lista[0].sort()
lista[1].sort()
print(f'Valores pares crescente: {lista[0]}')
print(f'Valores ímpares crescente: {lista[1]}')