# ex109 - modifique as funções que foram criadas no desafio 107 para que elas 
# aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não 
# formatado pela função moeda(), desenvolvida no desafio 108
import ex109
a = float(input('Digite o valor: R$ '))
print(f'Metade: {ex109.metade(a, True)}')
print(f'Dobro: {ex109.dobro(a, True)}')
print(f'+ 10%: {ex109.aumentar(a, 10, True)}')
print(f'- 15%: {ex109.diminuir(a, 15, True)}')