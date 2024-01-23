# ex110 - adicione ao módulo moeda.py criado nos desafios anteriores uma função
# chamada resumo(), que mostre na tela algumas informações geradas pelas funções
# que ja temos no módulo criado até aqui

import ex110
a = float(input('Digite o valor: R$ '))
print(f'Metade: {ex110.metade(a, True)}')
print(f'Dobro: {ex110.dobro(a, True)}')
print(f'+ 10%: {ex110.aumentar(a, 10, True)}')
print(f'- 15%: {ex110.diminuir(a, 15, True)}') 