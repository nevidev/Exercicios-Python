# crie um programa que leia dois valores e mostre um menu na tela
# somar, multiplicar, maior, novos números, sair do programa
# seu programa deverá realizar a operação solicitada em cada caso
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print('\n1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Novos números')
    print('5 - Sair')
    escolha = int(input('O que você quer desses 2 valores? '))
    if escolha == 1:
        result = n1 + n2
        print('R: A soma entre {} e {} resulta em {}'.format(n1, n2, result))
    elif escolha == 2:
        result = n1 * n2
        print('R: A multiplicação entre {} e {} resulta em {}'.format(n1, n2, result))
    elif escolha == 3:
        if n1 > n2:
            print('R: O número {} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('R: O número {} é maior que {}'.format(n2, n1))
        else:
            print('R: Os valores são iguais')
    elif escolha == 4:
        print('Informe 2 novos valores')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Programa encerrado\n')
    else:
        print('Opção inválida tente novamente')
    

