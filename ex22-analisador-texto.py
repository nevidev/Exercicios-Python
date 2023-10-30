# ex22 - crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas
# o nome com minúsculas
# quantas letras ao todo sem considerar espaços
# quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ').strip()
maiu = nome.upper()
minu = nome.lower()
tamanho = len(nome)
espacos = nome.count(' ')
dividir = nome.split()
nome1 = len(dividir[0])

print('letras maiúsculas: {}'.format(maiu))
print('letras minúsculas: {}'.format(minu))
print('seu nome possui {} letras'.format(tamanho - espacos))
print('seu primeiro nome tem {} letras'.format(nome1))
# outra maneira
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
