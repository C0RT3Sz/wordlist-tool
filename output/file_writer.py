def salvar_arquivo(lista_palavras, caminho_saida):
    try:
        with open(caminho_saida, "w", encoding="utf-8") as arquivo:
            for palavra in lista_palavras:
                arquivo.write(palavra + '\n')

    except OSError:
        print("Error de escrita")
    return
