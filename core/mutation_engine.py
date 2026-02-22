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


def gerar_variacoes_palavra(palavra):

    lista_variacoes = []

    lista_variacoes.append(palavra)

    metade = palavra[0:len(palavra)//2]
    lista_variacoes.append(metade)

    if len(palavra) >= 3:
        lista_variacoes.append(palavra[0:3])

    lista_variacoes.append(palavra.upper())
    lista_variacoes.append(palavra.capitalize())

    return lista_variacoes


def gerar_variacoes_numero(numero):

    lista_variacoes = []

    lista_variacoes.append(numero)

    if len(numero) >= 4:
        lista_variacoes.append(numero[-4:])

    if len(numero) >= 4:
        lista_variacoes.append(numero[0:4])

    return lista_variacoes


def gerar_variacoes(palavra):

    lista_variacoes = []

    lista_variacoes.append(palavra)

    metade = palavra[:len(palavra)//2]
    lista_variacoes.append(metade)

    if len(palavra) >= 3:
        tres_primeiro = palavra[:3]
        lista_variacoes.append(tres_primeiro)

    lista_variacoes.append(palavra.upper())
    lista_variacoes.append(palavra.capitalize())

    return lista_variacoes

def gerar_mutacoes_completas(lista_palavras, lista_numeros):

    lista_resultados = []

    for palavra in lista_palavras:
        variacoes_palavras = gerar_variacoes(palavra)

        for numero in lista_numeros:
            variacoes_numeros = gerar_variacoes_numero(numero)

            for vp in variacoes_palavras:
                for vn in variacoes_numeros:
                    combinacao = vp + vn

                    if validar_combinacoes(combinacao):
                        lista_resultados.append(combinacao)

    lista_resultados = remover_duplicados(lista_resultados)

    lista_resultados = filtrar_tamanho(lista_resultados, 16)

    return lista_resultados


def validar_combinacoes(texto):

    if not texto:
        return False
    if len(texto) < 2:
        return False

    return True


def remover_duplicados(lista_entrada):

    conjunto_vistos = set()
    lista_resultado = []

    for item in lista_entrada:

        if item not in conjunto_vistos:
            conjunto_vistos.add(item)
            lista_resultado.append(item)

    return lista_resultado

def filtrar_tamanho(lista_entrada, tamanho_maximo):

    lista_filtrada = []

    for item in lista_entrada:
        if len(item) <= tamanho_maximo:
            lista_filtrada.append(item)

    return lista_filtrada