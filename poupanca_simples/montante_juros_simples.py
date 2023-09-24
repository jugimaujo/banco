def juros_simples(capital, taxa, tempo, porcentagem=True):
    '''Função para calcular juros simples

    capital (float): é o investimento inicial;
    taxa (float): é a taxa de juros aplicada ao capital;
    tempo (float): é o tempo simulado de juros acumulados no capital;
    porcentagem (bool): "True" para a taxa passada em forma de porcentagem,
                        "False" para a taxa passada em forma normal.

    A unidade de tempo é hipotética
    A função só serve como um cálculo demonstrativo.'''

    if porcentagem:
        taxa /= 100

    return capital * taxa * tempo


def montante(capital, juros):
    '''Função para cálculo de montante

    capital (float): é o investimento inicial;
    juros (float): são os juros acumulados do investimento.'''

    return capital + juros
