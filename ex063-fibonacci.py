# ex63 - escreva um programa que leia um número n inteiro qualquer e mostre na tela 
# os n primeiros elementos de uma sequencia de fibonacci
# 0 1 1 2 3 5 8 13... (soma os 2 termos anteriores)
n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
print('{} {}'.format(t1, t2), end = ' ')
cont = 3
while cont <= n:
    t3 = t2 + t1
    print('{}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('fim')