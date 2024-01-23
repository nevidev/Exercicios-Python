# ex29 - escreva um programa que leia a velocidade de um carro
# se ultrapassar 80km/h recebe multa
# a multa custa R$ 7 por cada Km acima do limite
multa = int(input('Qual velocidade ele estava? '))
if (multa > 80):
    print('A multa foi no valor de R$ {}'.format((multa-80)*7))
else:
    print('Estava dentro do limite permitido de 80Km/h')