from core.input_processor import processar_entrada
from core.mutation_engine import gerar_mutacoes_completas
from output.file_writer import salvar_arquivo

def arquivo_nao_existe(caminho):
    import os
    return not os.path.exists(caminho)

def main():
    print(" === Wordlist Tool Iniciada === ")
    caminho_arquivo = input("Passe o arquivo do alvo: ")

    if not caminho_arquivo:
        print("Nenhum caminho informado")
        return

    if arquivo_nao_existe(caminho_arquivo):
        print("Arquivo não encontrado")
        return

    caminho_saida = "resultado.txt"

    lista_palavras, lista_numeros = processar_entrada(caminho_arquivo)

    wordlist_final = gerar_mutacoes_completas(lista_palavras, lista_numeros)

    salvar_arquivo(wordlist_final, caminho_saida)

    print("Wordlist criada com sucesso")

if __name__ == "__main__":
    main()