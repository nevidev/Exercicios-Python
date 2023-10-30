# ex44 - elabora um programa que calcule o valor a ser pago por um produto, considerando
# seu preço normal e condição de pagamento
# a vista dinheiro/pix : 10% de desconto
# a vista no cartão: 5% de desconto
# até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
preco = float(input('Digite o valor do produto: '))
pag = input('Digite o método de pagamento: ').strip()
vezes = int(input('Digite a quantidade de parcelas: '))
if (pag.upper() == 'DINHEIRO' or pag.upper() == 'PIX') and vezes == 1:
    print('Com 10% de desconto, o item ficou no valor de R$ {}'.format(preco*0.9))
elif (pag.upper() == 'CARTÃO' or pag.upper() == 'CARTAO') and vezes == 1:
    print('Você obteve 5% de desconto, o item custou R$ {}'.format(preco*0.95))
elif (pag.upper() == 'CARTÃO' or pag.upper() == 'CARTAO') and vezes == 2:
    print('Você não obteve descontos, o item custará R$ {}'.format(preco))
else:
    print('Parcelando em {} vezes, dado 20% de juros, o preço do item fica em R$ {}'.format(vezes, preco*1.2))
