# ex42 - refaça o ex35 dos triângulos acrescentando o recurso de mostrar que tipo 
# de triângulo será formado:
# equilátero: todos os lados iguais
# isósceles: dois lados iguais
# escaleno: todos os lados diferentes
r1 = int(input('Qual o comprimento da reta 1? '))
r2 = int(input('Qual o comprimento da reta 2? '))
r3 = int(input('Qual o comprimento da reta 3? '))
if ((r1 > abs(r2-r3) and r1 < (r2+r3)) or (r2 > abs(r1-r3) and r2 < (r1+r3)) or (r3 > abs(r2-r1) and r3 < (r2+r1))):
    print('É possível se fazer um triângulo')
    if r1 == r2 == r3:
        print('Forma-se um triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Forma-se um triângulo isósceles')
    else:
        print('Forma-se um triângulo escaleno')
else:
    print('Não é possível se formar um triângulo')