# ex26 - faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra A
# em que posição aparece ela a primeira vez
# em que posição ela aparece a ultima vez
frase = input('Digite uma frase: ').strip()
a = frase.upper().count('A')
print('A letra A apareceu {} vezes'.format(a))
a1 = frase.upper().find('A')
print('A letra A apareceu primeiro na posição {}'.format(a1 + 1))
a2 = frase.upper().rfind('A')
print('A letra A apareceu por último na posição {}'.format(a2 + 1))