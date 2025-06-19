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
# def qtde_valores_unicos(lista: list) -> int:
#     lista_unica: list = list(set(lista))
#     return lista_unica
# lista_transformada: list = qtde_valores_unicos([2, 3, 4, 4, 4])
# print(f"Os numeros que compoe a lista sao: {lista_transformada}, com uma quantidade de {len(lista_transformada)} numeros.")
# correcao ex. 3
# def contar_valores_unicos(lista: list[int]) -> int:
#     return len(set(lista))

# 4. Converter Celsius para Fahrenheit em uma Lista
# def celsius_para_fahrenheit(celsius: float) -> float:
#     return (celsius * 9/5) + 32
# conversao: float = celsius_para_fahrenheit(25)
# print(f"F {conversao}")
# correcao ex. 4
# def celsius_para_fahrenheit(temperaturas_celsius: list[float]) -> list[float]:
#     return [(9/5) * temp + 32 for temp in temperaturas_celsius]

# 5. Calcular Desvio Padrão de uma Lista
# import statistics
# def calcular_desvio_padrao_de_uma_lista(lista_numeros: list[float]) -> float:
#     return round(statistics.stdev(lista_numeros), 2)
# desvio_padrao_calculado: float = calcular_desvio_padrao_de_uma_lista([10, 12, 23, 23, 16, 23, 21, 16])
# print(desvio_padrao_calculado)
# # correcao ex. 5
# def calcular_desvio_padrao(valores: List[float]) -> float:
#     media = sum(valores) / len(valores)
#     variancia = sum((x - media) ** 2 for x in valores) / len(valores)
#     return variancia ** 0.5

# 6. Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: list[int]) -> list[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

lista_setada: list[int] = [23, 12, 13, 1]

valores_ausentes: list[int] = encontrar_valores_ausentes(lista_setada)

print(valores_ausentes)