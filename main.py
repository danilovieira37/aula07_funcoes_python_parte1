from etl import ler_csv, filtrar_produtos_entregues, somar_valores_dos_produtos

path_arquivo = "vendas.csv"

lista_de_produtos: list[dict] = ler_csv(path_arquivo)
produtos_entregues: list[dict] = filtrar_produtos_entregues(lista_de_produtos)
valor_dos_produtos_entregues: list[dict] = somar_valores_dos_produtos(produtos_entregues)
print(f"lista de produtos completa: {lista_de_produtos}")

print(f"Lista filtrada com true na entrega: {produtos_entregues}")

print(valor_dos_produtos_entregues)