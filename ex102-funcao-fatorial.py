# ex102 - crie um programa que tenha uma função fatorial() que receba dois parâmetros
# o primeiro que indique o numero para calcular e o outro chamado show, que será
# o valor lógico (opcional) indicando se será mostrado ou não na tela o processo
# de calculo do fatorial

def fatorial(num, show=False):
    """ Calcula o fatorial de um número
    num: número escolhido
    show: opcional -> se você quer ver a conta (True) ou não (False)
    """
    x = 1
    while num <= 0:
        return "Valor tem que ser maior que zero!"
    for v in range(num, 0, -1):
        if show:
            if v > 1:
                print(f'{v} * ', end='')
            elif v == 1:
                print(f'{v} = ', end='')
        x = x * v
    return x

print(fatorial(6, False))
help(fatorial)
    

