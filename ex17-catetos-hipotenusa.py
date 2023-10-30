# ex17 - faça um programa que leia o comprimento do cateto oposto e 
# do adjacente de um triângulo retângulo, calcule e mostre o comprimento
# da hipotenusa
from math import hypot
catop = int(input('Cateto oposto: '))
catad = int(input('Cateto adjacente: '))
hipotenusa = hypot(catop, catad)
print('Cateto oposto de valor {} e adjacente de valor {} resulta \
em uma hipotenusa de valor {:.2f}'. format(catop, catad, hipotenusa))