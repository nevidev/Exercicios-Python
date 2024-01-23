# ex38 - escreva um programa que leia dois números inteiros e compare-os, mostrando
# na tela uma mensagem:
# o primeiro valor é o maior, o segundo valor é o maior, não existe valor maior
# os dois são iguais
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro número é maior.'.format(n1))
elif n1 < n2:
    print('O segundo número é maior.'.format(n2))
else:
    print('Os números são iguais.')