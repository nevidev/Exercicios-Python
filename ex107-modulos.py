# ex107 - crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro(), metade()
# faça também um programa que importe esse módulo e use algumas dessas funções

import ex107
a = float(input('Digite um valor: '))
print(f'Metade: {ex107.metade(a)}')
print(f'Dobro: {ex107.dobro(a)}')
print(f'+ 10%: {ex107.aumentar(a, 10):.2f}')
print(f'- 15%: {ex107.diminuir(a, 15):.2f}')