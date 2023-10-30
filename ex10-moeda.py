# ex10 - crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ele pode comprar
# considere o dolar a R$ 3,27
grana = float(input('Quantos reais você tem? '))
dolar = 3.27

result = grana / dolar
print('Com {} reais você pode comprar {:.2f} dólares'.format(grana, result))