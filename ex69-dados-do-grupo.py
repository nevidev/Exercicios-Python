# ex69 - crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa 
# cadastrada o programa deverá perguntar se o usuário quer ou não continuar. 
# No final mostre: quantas pessoas tem +18 anos, quantos homens foram cadastrados
# quantas mulheres têm menos de 20 anos
qidade = 0
qhomens = 0
qmulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite o sexo: (M/F) ').strip().upper()[0]
    if idade > 18:
        qidade += 1
    if sexo == 'M':
        qhomens += 1
    if idade < 20 and sexo == 'F':
        qmulheres += 1
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar o cadastro? (S/N) ').strip().upper()[0]
    if cont == 'N':
        break
print(f'{qidade} pessoas têm mais de 18 anos, {qhomens} são homens e {qmulheres}\
 são mulheres com menos de 20 anos')
