# ex67 - faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo
while True:
    n = int(input('Tabuada do valor: '))
    tab = 1
    while tab < 10:
        if n <= 0:
            print('Programa encerrado...')
            break
        print(f'{n} x {tab} = {n*tab}')
        tab += 1
    print('')


