# desenvolva uma calculadora de imc
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC possui valor de {:.2f}, logo, você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC possui valor de {:.2f}, logo, você está com peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC possui valor de {:.2f}, logo, você está com sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC possui valor de {:.2f}, logo, você está com obesidade'.format(imc))
else:
    print('Seu IMC possui valor de {:.2f}, logo, você está com obesidade'.format(imc))