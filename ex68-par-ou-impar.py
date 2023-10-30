# ex68 - faça um programa que jogue par ou impar com o computador. O jogo só será
# interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
from random import randint
jogadas = 0
while jogadas >= 0:
    n = int(input('Jogue um número: '))
    escolha = str(input('Você quer par ou ímpar? (P/I) ')).strip().upper()[0]
    n2 = randint(0, 10)
    jogadas += 1
    if escolha == 'P' and (n + n2) % 2 == 0:
        print(f'A soma deu {n + n2}, par, você ganhou!')
    elif escolha == 'I' and (n + n2) % 2 != 0:
        print(f'A soma deu {n + n2}, ímpar, você ganhou!')
    elif escolha == 'P' and (n + n2) % 2 != 0:
        print(f'A soma deu {n + n2}, ímpar, você perdeu!')
        break
    elif escolha == 'I' and (n + n2) % 2 == 0:
        print(f'A soma deu {n + n2}, par, você perdeu!')
        break
    else:
        print('Tente novamente')
print(f'Você ganhou {jogadas - 1} partidas seguidas')

    
