# ex24 - crie um programa que leia o nome de uma cidade e diga se ela começa 
# ou não com o nome "santo"
cidade = input('Digite o nome de uma cidade: ').strip()
maiu = cidade.upper()
corte = maiu.split()
santo = ('SANTO' in corte[0])
if (santo == True):
    print('A cidade mencionada começa com Santo')
else:
    print('A cidade não começa com Santo')
