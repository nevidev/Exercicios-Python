# ex31 - desenvolva um programa que pergunte a distância de uma viagem em Km
# calcule o preço da passagem, sobrando R$ 0,50 por Km para viagens até 200Km
# e R$ 0,45 para viagens mais longas
viagem = int(input('Qual a distância da viagem em Km? '))
if (viagem <= 200):
    print('O preço da viagem fica em R${:.2f}'.format(viagem*0.5))
else:
    print('O preço da viagem fica em R${:.2f}'.format(viagem*0.45))