# ex61 - refaça o desafio 51 lendo o primeiro termo e a razão de uma PA, mostrando os 10
# primeiros termos da progressão usando a estrutura while

n1 = int(input('Digite um número para começar a PA: '))
r = int(input('Digite e razão da PA: '))
i = 0
print(n1)
while i < 9:
    n1 = n1 + r
    i = i + 1
    print('{}'.format(n1))
