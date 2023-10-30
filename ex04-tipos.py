# ex4 - faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele

algo = input('Digite algo: ')
print('o tipo primitivo é', type(algo))
print('só tem espaços? ', algo.isspace())
print('é um número? ', algo.isnumeric())
print('é alfabético? ', algo.isalpha())
print('é alfanumérico? ', algo.isalnum())
print('está tudo em maiúsculo? ', algo.isupper())
print('está tudo em minúsculo? ', algo.islower())
print('está capitalizada(tem maiúscula e minúscula)? ', algo.istitle())