# ex57 - faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# 'M' ou 'F'.
# caso esteja errado peça a digitação novamente até ter um valor correto
sexo = str(input('Digite o sexo (M/F): ')).strip().upper()
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Digite somente M ou F: ')).strip().upper()
    if sexo == 'M':
        print('Sexo masculino')
        break
    elif sexo == 'F':
        print('Sexo feminino')
        break
