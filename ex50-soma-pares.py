# ex50 - desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares, se for impar desconsiderar
s = 0
for i in range(0,6):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        s = s + n1
print('A soma dos pares ficou em: {}'.format(s))