import csv

path_arquivo: str = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """"
    Funcao que le um arquivo csv e retorna uma lista
    de dicionarios
    """
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

vendas_itens: list[dict] = ler_csv(path_arquivo)
print(vendas_itens)