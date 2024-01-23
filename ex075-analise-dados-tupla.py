# ex75 - desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
# uma tupla. Mostre: quantas vezes aparece o valor 9, em que posição foi digitado
# o primeiro valor 3, quais foram os números pares
cont9 = 0
cont3 = 0
n0 = int(input('Digite um valor inteiro: '))
n1 = int(input('Digite outro valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
n3 = int(input('Digite o último valor inteiro: '))
tupla = (n0, n1, n2, n3)

if 9 in tupla:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')
else:
    print('O valor 9 não foi digitado')
if 3 in tupla:
    print(f'O valor 3 foi digitado a primeira vez na posição {tupla.index(3)+1}')
else:
    print('O valor 3 não foi digitado')

print(f'Números pares: ', end='')
for t in tupla:
    if t % 2 == 0:
        print(t, end=' ')
