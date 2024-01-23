# ex78 - faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final
# mostre qual foi o maior valor e o menor, e suas posições na lista
lista = []
maior = 0
menor = 0

for v in range(0,5):
    lista.append(int(input('Digite um valor inteiro: ')))
    if v == 0:
        maior = lista[v]
        menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]

print(f'Maior: {maior}, na posição ->', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}', end=' ')
print(f'\nMenor: {menor}, na posição ->', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}', end=' ')

