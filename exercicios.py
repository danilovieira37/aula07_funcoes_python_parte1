# ex. 1
# 1. Calcular Média de Valores em uma Lista
# from typing import List
# def media_de_uma_lista(lista: List[float]) -> float:
#     return sum(lista) / len(lista)
# valores = [2, 2]
# print(media_de_uma_lista(valores))

# 2. Filtrar Dados Acima de um Limite
# lista_filtrada: list = []
# def filtrar_dados_acima_de_um_limite(lista: list, limite: int) -> list:
#     for n in lista:
#         if n > limite:
#             lista_filtrada.append(n)
#     return lista_filtrada
# filtro: list = filtrar_dados_acima_de_um_limite([2,3,4,6,78,88,89], 5)
# print(filtro)
# correcao ex. 2
# def filtrar_acima_de(valores: list[float], limite: float) -> list[float]:
#     resultado = []
#     for valor in valores:
#         if valor > limite:
#             resultado.append(valor)
#     return resultado

# 3. Contar Valores Únicos em uma Lista
def qtde_valores_unicos(lista: list) -> int:
    lista_unica: list = list(set(lista))
    return lista_unica

lista_transformada: list = qtde_valores_unicos([2, 3, 4, 4, 4])

print(f"Os numeros que compoe a lista sao: {lista_transformada}, com uma quantidade de {len(lista_transformada)} numeros.")