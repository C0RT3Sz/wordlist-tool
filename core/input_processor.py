def ler_arquivo(caminho_arquivo):

    lista_linhas = []

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
           for linha in arquivo:
               lista_linhas.append(linha.strip())

    except FileNotFoundError:
        print("Error ao ler arquivo.")
        return []

    return lista_linhas


def processar_entrada(caminho_arquivo):

    linhas = ler_arquivo(caminho_arquivo)

    linhas_normalizadas = normalizar_linhas(linhas)

    lista_palavra, lista_numeros = separar_palavras_e_numeros(linhas_normalizadas)

    return lista_palavra, lista_numeros


def normalizar_linhas(lista_linhas):

    lista_normalizada = []

    for linha in lista_linhas:
        linha_limpa = linha.strip()
        linha_limpa = linha_limpa.lower()

        if linha_limpa:
            lista_normalizada.append(linha_limpa)

    return lista_normalizada


def separar_palavras_e_numeros(lista_entrada):
    lista_palavras = []
    lista_numero = []

    for item in lista_entrada:
        if item.isdigit():
            lista_numero.append(item.strip())
        else:
            lista_palavras.append(item.strip())

    return  lista_palavras, lista_numero