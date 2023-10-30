# ex11 - faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2m² 
altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
area = altura * largura
tinta = area / 2

print('A área a ser pintada é de {}m², logo a quantidade de tinda necessária é de {}L'.format(area, tinta))