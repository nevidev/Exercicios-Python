# ex101 - crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
# indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições
from datetime import date
def voto(nasc):
    global idade
    dataHoje = date.today()
    ano = dataHoje.strftime('%Y')
    idade = int(ano) - nasc
    if idade < 16:
        return "negado"
    elif (idade >= 16 and idade < 18) or (idade >= 65):
        return "opcional"
    else:
        return "obrigatório"

anoNasc = int(input('Em que ano você nasceu? '))
result = voto(anoNasc)
print(f'Você está com ou fará: {idade} anos')
print(f'Seu voto está como: {result}')
