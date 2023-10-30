# ex8 - escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros
n1 = int(input('Digite o valor em metros: '))
print('O valor em centímetros equivale a {:.0f}cm e em milímetros equivale a {:.0f}mm'.format(n1 * 100, n1 * 1000))