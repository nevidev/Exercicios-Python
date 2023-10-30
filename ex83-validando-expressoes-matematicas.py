# ex83 - crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está com os
# parênteses abertos e fechados na ordem correta

lista = []
p1 = 0
p2 = 0

p = input('Digite sua expressão: ')

for v in p:
    if v == '(':
        lista.append('(')

    elif v == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')

