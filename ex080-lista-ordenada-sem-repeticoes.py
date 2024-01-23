# ex80 - crie um programa onde o usuário possa digitar 5 valores e cadastrar numa lista
# ja na posição correta (sem usar o sort). No final mostre a lista
lista = []
for v in range(0,5):
    n = int(input('Digite um número: '))
    if v == 0:
        lista.append(n)
        print('Primeiro valor adicionado')
    elif n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista')
    else:
        meio = 0
        while meio < len(lista):
            if n <= lista[meio]:
                lista.insert(meio, n)
                print(f'Valor adicionado na posição {meio}')
                break
            meio += 1
  
print(f'Os valores em ordem crescente ficaram: {lista}')

