# ex108 - adapte o codigo do desafio 107, criando uma função adicional chamada
# moeda() que consiga mostrar os valores como um valor monetário formatado

import ex108
a = float(input('Digite um valor: R$ '))
print(f'Metade: {ex108.moeda(ex108.metade(a))}')
print(f'Dobro: {ex108.moeda(ex108.dobro(a))}')
print(f'+ 10%: {ex108.moeda(ex108.aumentar(a, 10))}')
print(f'- 15%: {ex108.moeda(ex108.diminuir(a, 15))}')