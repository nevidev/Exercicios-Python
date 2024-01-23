# ex27 - faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o ultimo nome separadamente
nome = input('Qual seu nome completo? ').strip()
nome1 = nome.split()
print('O primeiro nome é {} e o ultimo é {}'.format(nome1[0], nome1[len(nome1)-1]))
print(len(nome1))