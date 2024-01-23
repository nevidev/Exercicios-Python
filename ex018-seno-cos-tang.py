# ex18 - faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo
from math import tan, sin, cos
n1 = int(input('Digite um ângulo: '))
print('O ceno desse ângulo é de {:.2f}, o cosseno é de {:.2f} \
e a tangente é de {:.2f}'.format(sin(n1), cos(n1), tan(n1)))