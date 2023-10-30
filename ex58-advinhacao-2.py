# ex58 - melhore o jogo do desafio 28 onde o computador vai "pensar"
# em um número entre 0 e 10. 
# só que agora o jogador vai tentar advinhar até acertar
# mostrando no final quantos palpites foram necessários para vencer
from random import randint
pc = randint(0, 10)
vezes = 1
num = int(input('Digite um número de 0 a 10: '))
while num != pc:
    vezes = vezes + 1
    num = int(input('Tente de novo: '))
    if num == pc:
        print('Acertou, era o número {}. Você gastou {} tentativas'.format(num, vezes))
        break

