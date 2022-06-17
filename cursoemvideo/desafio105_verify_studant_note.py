def notas(*num, sit=False):
    '''
    -> funcao para analisar notas e situacao do aluno
    :param num: pode ser inseridas uma ou mais notas
    :param sit: valor opcional mostando a situacao do aluno
    :return: analise de informacoes das notas
    '''
    tot = maiore = menore = soma = 0
    media1 = 1
    situa = ''
    for v in num:
        tot += 1
        soma +=v
        if tot == 1:
            maiore = menore = v
        else:
            if v > maiore:
                maiore = v
            if v < menore:
                menore = v
    media1 = soma / tot
    if media1 > 8.5:
        situa = 'Parabens'
    if media1 <= 8.5 and media1 >= 7:
        situa = 'Bom'
    if media1 < 7 and media1 >= 5:
        situa = 'Razoavel'
    if media1 < 5:
        situa = 'Ruim'
    aluno = {'total': tot, 'maior': maiore, 'menor': menore, 'media': media1}
    if sit:
        aluno['situação'] = situa
    return aluno


resp = notas(9, 10, 8.5, 10, 7, 8, sit=True)
print(resp)