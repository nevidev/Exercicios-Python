# ex45 - crie um programa que faça o computador jogar jokenpô com vc
import random
print('Pedra')
print('Papel')
print('Tesoura')
arma = str(input('Escolha sua arma: ')).strip()
lista = ['Pedra', 'Papel', 'Tesoura']
if arma.upper() == 'PEDRA' and random.choice(lista).upper() == 'PEDRA':
    print('O computador escolheu pedra, EMPATE')
elif arma.upper() == 'PEDRA' and random.choice(lista).upper() == 'TESOURA':
    print('O computador escolheu tesoura, VOCÊ GANHOU')
elif arma.upper() == 'PEDRA' and random.choice(lista).upper() == 'PAPEL':
    print('O computador escolheu papel, VOCÊ PERDEU')
elif arma.upper() == 'PAPEL' and random.choice(lista).upper() == 'PAPEL':
    print('O computador escolheu papel, EMPATE')
elif arma.upper() == 'PAPEL' and random.choice(lista).upper() == 'PEDRA':
    print('O computador escolheu pedra, VOCÊ GANHOU')
elif arma.upper() == 'PAPEL' and random.choice(lista).upper() == 'TESOURA':
    print('O computador escolheu tesoura, VOCÊ PERDEU')
elif arma.upper() == 'TESOURA' and random.choice(lista).upper() == 'TESOURA':
    print('O computador escolheu tesoura, EMPATE')
elif arma.upper() == 'TESOURA' and random.choice(lista).upper() == 'PAPEL':
    print('O computador escolheu papel, VOCÊ GANHOU')
elif arma.upper() == 'TESOURA' and random.choice(lista).upper() == 'PEDRA':
    print('O computador escolheu pedra, VOCÊ PERDEU')
elif arma.upper() != 'PEDRA' or arma.upper() != 'TESOURA' or arma.upper() != 'PAPEL':
    print('Opção inválida')
print('')
# MANEIRA COM MENU DE ESCOLHA
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
arma2 = int(input('Escolha sua arma de acordo com o número: '))
if arma2 == 1 and random.randint(1,3) == 1:
    print('O PC escolheu pedra, empatou')
elif arma2 == 1 and random.randint(1,3) == 2:
    print('O PC escolheu papel, você perdeu')
elif arma2 == 1 and random.randint(1,3) == 3:
    print('O PC escolheu tesoura, você ganhou')
elif arma2 == 2 and random.randint(1,3) == 1:
    print('O PC escolheu pedra, você ganhou')
elif arma2 == 2 and random.randint(1,3) == 2:
    print('O PC escolheu papel, empatou')
elif arma2 == 2 and random.randint(1,3) == 3:
    print('O PC escolheu tesoura, você perdeu')
elif arma2 == 3 and random.randint(1,3) == 1:
    print('O PC escolheu pedra, você perdeu')
elif arma2 == 3 and random.randint(1,3) == 2:
    print('O PC escolheu papel, você ganhou')
elif arma2 == 3 and random.randint(1,3) == 3:
    print('O PC escolheu tesoura, empatou')

