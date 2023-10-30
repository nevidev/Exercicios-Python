# ex37 - escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão
# 1 para binário, 2 para octal, 3 para hexadecimal
num = int(input('Digite um número inteiro: '))
print('1 - binário')
print('2 - octal')
print('3 - hexadecimal')
escolha = int(input('Escolha o método de conversão: '))
if escolha == 1:
    print('O valor convertido em binário é: {}'.format(bin(num)[2:]))
elif escolha == 2:
    print('O valor convertido em binário é: {}'.format(oct(num)[2:]))
elif escolha == 3:
    print('O valor convertido em binário é: {}'.format(hex(num)[2:]))
else:
    print('Opção não existente')
    