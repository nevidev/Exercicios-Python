# ex34 - escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento
# para salários superiores a R$ 1250 calcule um aumento de 10%
# para salários inferiores ou iguais, o aumento é de 15%
sal = int(input('Qual o salário a ser analisado? '))
if (sal > 1250):
    print('O aumento salarial para o valor {} vai resultar em {}'.format(sal, sal*0.1))
else:
    print('O aumento salarial para o valor {} vai resultar em {}'.format(sal, sal*0.15))