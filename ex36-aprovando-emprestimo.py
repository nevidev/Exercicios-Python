# ex36 - escreva um programa para aprovar um empréstimo bancário para a compra de uma
# casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos 
# anos ele vai pagar
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado
casa = int(input('Qual o valor da casa? '))
sal = int(input('Qual seu salário? '))
emp = int(input('Em quantos anos você vai pagar? '))
mes = emp * 12
if (casa / mes) <= (0.3*sal):
    print('Empréstimo aprovado')
else:
    print('Empréstimo negado')