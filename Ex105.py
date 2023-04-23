def notas(*n, sit=False):
    """
    Função para armazenar notas, mostrar média e situação de um Aluno
    :param n: lista de notas do aluno.
    :param sit: (opcional) Mostra a situação de um Aluno de acordo com a média.
    :return: dicionário com informações sobre as notas, média e situação.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] <= 6:
            r['situação'] = 'Reprovado'
        else:
            r['situação'] = 'Aprovado'
    return r

# Programa Principal
resp = notas(4.5,5.6,7.3,sit=True)
print(resp)
