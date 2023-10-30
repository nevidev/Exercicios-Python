# ex51 - desenvolva um programa que leia o primeiro termo e a razão de uma PA
# mostre os 10 primeiros termos dessa progressão
n1 = int(input('Digite um número inteiro: '))
pa = int(input('Digite a razão da PA: '))
print('Os 10 primeiros valores, começando de {} com razão {}, são:'.format(n1,pa))
print(n1)
for i in range(1,10):
    n1 = pa + n1
    print(n1)
print('-'*20)

# outra maneira
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i), end=', ')
print('FIM')
