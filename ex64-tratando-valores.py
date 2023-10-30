# ex64 - crie um programa que leia vários números inteiros pelo teclado. O programa
# só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
n1 = int(input('Digite um número: '))
n2 = 0
qtd = 0
while n1 != 999:
    n1 = int(input('Digite um número: '))
    n2 = n2 + n1
    qtd += 1
    if n2 == 999:
        break
print('Foram digitados {} números e a soma dos números digitados deu {}'.format(qtd, n2 - 999))
