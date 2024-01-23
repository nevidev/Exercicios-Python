# ex35 - desenvolva um programa que leia o comprimento de tres retas e diga ao usuário
# se elas podem ou não formar um triangulo
# obs: um dos lados deve ser maior que a diferença dos outros 2 lados e
# menor que a soma dos outros 2 lados
r1 = int(input('Qual o comprimento da reta 1? '))
r2 = int(input('Qual o comprimento da reta 2? '))
r3 = int(input('Qual o comprimento da reta 3? '))
if ((r1 > abs(r2-r3) and r1 < (r2+r3)) or (r2 > abs(r1-r3) and r2 < (r1+r3)) or (r3 > abs(r2-r1) and r3 < (r2+r1))):
    print('É possível se fazer um triângulo')
else:
    print('Não é possível se formar um triângulo')