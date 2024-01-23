# ex62 - melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos
n1 = int(input('Digite um número para mostrar sua PA: '))
r = int(input('Digite a razão dessa PA: '))
i = 1
j = 0
t = 10
print(n1)
while t != 0:
    j = j + t
    while i < j:
        i = i + 1
        n1 = n1 + r
        print(n1)
    t = int(input('Quer ver mais quantos termos? '))
print('Programa encerrado')
