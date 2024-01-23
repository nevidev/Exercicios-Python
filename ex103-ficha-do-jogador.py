# ex103 - faça um programa que tenha uma função chamada ficha(), que receba dois 
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou
# o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
# não tenha sido informado corretamente

def ficha(nome='<desconhecido>', gols=0):
    nome = input('Digite o nome: ').strip()
    gols = input('Quantos gols foram feitos: ').strip()
    if gols == '':
        gols = int(0)
    if nome == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gols na partida.'

print(ficha())

