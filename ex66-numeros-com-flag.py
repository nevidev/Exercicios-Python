# ex66 - crie um programa que leia varios números inteiros pelo teclado. o Programa
# só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitaros e qual foi a soma entre eles
soma = num = n1 = 0
while n1 != 999:
    n1 = int(input('Digite um número: '))
    if n1 == 999:
        break
    soma += n1
    num += 1
print(f'Foram digitados {num} números e a soma entre eles foi de {soma}')
