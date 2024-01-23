# ex105 - faça um programa que tenha uma função notas() que pode receber varias
# notas de alunos e vai retornar um dicionário com as seguintes infos:
# quantidade de notas; a maior nota; a menor nota; a média da turma; a situação(opcional)
# adicione também as docstrings da função

def notas(*n, sit=False):
    """ função para analisar notas de vários alunos
    n: uma ou várias notas
    sit: opcional para mostrar a situação do aluno
    return: dicionário com as informações
    """
    dic = {}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = sum(n) / len(n)

    if sit:
        if dic['media'] >= 8:
            dic['situacao'] = 'Boa'
        elif dic['media'] >= 6:
            dic['situacao'] = 'Média'
        else:
            dic['situacao'] = 'Ruim'
    return dic



# main
resp = notas(10, 8, 10, 6.5, sit=True)
print(resp)
help(notas)