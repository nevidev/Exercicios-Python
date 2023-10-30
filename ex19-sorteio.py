# ex19 - um professor quer sortear um dos quatro alunos para apagar
# o quadro, faça um programa que ajude ele, lendo o nome deles e escrevendo
# o nome escolhido
import random
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
sorteio = random.choice(lista)
print('O aluno escolhido foi: {}'.format(sorteio))