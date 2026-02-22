def combinar_palavra_com_numero(palavra, numero):

    combinacao = palavra + str(numero)

    return combinacao


def gerar_mutacoes(lista_palavras, lista_numeros):

    lista_resultados = []

    for palavra in lista_palavras:
        for numero in lista_numeros:
            combinacao = combinar_palavra_com_numero(palavra, numero)
            lista_resultados.append(combinacao)

    return lista_resultados
