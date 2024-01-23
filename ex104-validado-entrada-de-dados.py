# ex104 - crie um programa que tenha a função leiaInt() que vai funcionar de forma
# semelhante à função input() do Python, só que fazendo a validação para aceitar
# apenas um valor numérico
# ex: n = leiaInt('Digite um n')

def leiaInt(msg):
    ok = False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print('\033[0;31merro, digite um número!\033[m')
        if ok:
            break
    return num

# main
n = leiaInt('Digite um número: ')
print(f'Você digitou {n}')
