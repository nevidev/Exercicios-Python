# ex20 - o mesmo professor quer sortear a ordem de apresentação de
# trabalhos dos alunos. faça um programa que leia o nome dos quatro
# alunos e mostre a ordem sorteada
import random
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)