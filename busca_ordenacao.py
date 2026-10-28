def busca_sequencial(registros, codigo):
    comparacoes = 0
    for i in range(len(registros)):
        comparacoes += 1
        if registros[i]["codigo"] == codigo:
            return i, comparacoes
    return -1, comparacoes

def busca_binaria(registros, codigo):
    inicio = 0
    fim = len(registros) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if registros[meio]["codigo"] == codigo:
            return meio, comparacoes
        elif registros[meio]["codigo"] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes

def ordenar_insercao(registros, chave):
    lista = registros[:]
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j][chave] > atual[chave]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
    return lista
