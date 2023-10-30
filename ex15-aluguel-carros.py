# ex15 - escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$ 0,15 por Km rodado
n1 = float(input('Quantos dias alugado? '))
n2 = float(input('Quantos Km rodados? '))

# valores em R$
dias = 60
km = 0.15
print('O valor total ficou em R$ {:.2f}'.format((n1 * dias) + (n2 * km)))