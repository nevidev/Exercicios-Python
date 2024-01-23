# ex106 - faça um mini sistema que utilize o intactive help do Python
# o usuário vai digitar o comando e o manual vai aparecer
# quando o usuário digitar a palavra 'fim' o programa se encerrará

def ajuda(com):
    help(com)
def title(msg):
    tam = len(msg)
    print('-' * tam)
    print(msg)
    print('-' * tam)
# main
while True:
    title('Sistema de ajuda')
    cmd = str(input('Digite a função: '))
    if cmd.upper() == 'FIM':
        break
    else:
        ajuda(cmd)
title('Até mais!')