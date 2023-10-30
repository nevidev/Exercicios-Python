# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# no final mostre: a média da idade do grupo
# nome do homem mais velho
# quantas mulheres têm menos de 20 anos
soma = 0
idadevelho = 0
nomevelho = ''
mulheres = 0
for i in range(1,5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i))).strip()
    idade = int(input('Qual a idade da {}ª pessoa: '.format(i)))
    sexo = input('Digite o sexo da {}ª pessoa (M/F): '.format(i)).upper().strip()
    soma = soma + idade
    media = soma / i
    if sexo == 'M' and i == 1:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
print('Há {} mulheres com menos de 20 anos'.format(mulheres))
print('Homem mais velho: {}, com {} anos'.format(nomevelho, idadevelho))
print('A média das idades é de {:.2f} anos'.format(media))
    
