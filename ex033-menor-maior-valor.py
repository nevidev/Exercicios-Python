# ex33 - faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = int(input('Digite o terceiro número inteiro: '))
if (n1 < n2 and n1 < n3 and n2 < n3):
    print('O menor número é {} e o maior é {}'.format(n1, n3))
elif (n2 < n1 and n2 < n3 and n1 < n3):
    print('O menor número é {} e o maior é {}'.format(n2, n3))
elif (n3 < n1 and n3 < n2 and n1 < n2):
    print('O menor número é {} e o maior é {}'.format(n3, n2))
elif (n3 < n1 and n3 < n2 and n1 > n2):
    print('O menor número é {} e o maior é {}'.format(n3, n1))
elif (n3 < n1 and n3 < n2 and n1 > n3):
    print('O menor número é {} e o maior é {}'.format(n2, n1))
elif (n1 < n2 and n1 < n3 and n2 > n3):
    print('O menor número é {} e o maior é {}'.format(n1, n2))