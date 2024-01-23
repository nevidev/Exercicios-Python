def metade(n = 0, formatado = False):
    num = n / 2
    return f'{num:.2f}' if formatado == False else moeda(num)

def dobro(n = 0, formatado = False):
    num = n * 2
    return num if formatado == False else moeda(num)

def aumentar(n = 0, p = 0, formatado = False):
    num = n + (n * (p / 100))
    return num if formatado == False else moeda(num)

def diminuir(n = 0, p = 0, formatado = False):
    num = n - (n * (p / 100))
    return num if formatado == False else moeda(num)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')