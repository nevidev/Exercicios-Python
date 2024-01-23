# ex77 - crie um programa que tenha uma tupla com várias palavras(sem acento).
# Depois mostre, para cada palavra, quais são suas vogais

palavras = ('Omen', 'Zeri', 'Jett', 'Gekko', 'Jinx', 'Spike')
for p in palavras:
    print(f'\nEm "{p}" temos as vogais: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(f'{letra.upper()}', end=' ')
