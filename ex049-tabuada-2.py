# ex49 - refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
# um laço for
n1 = int(input('Digite um número inteiro: '))
print('Tabuada do número {}: '.format(n1))
for i in range(1, 10):
    print('{} x {} = {}'.format(n1, i, n1*i))