# ex. 1
# 1. Calcular Média de Valores em uma Lista
from typing import List
def media_de_uma_lista(lista: List[float]) -> float:
    return sum(lista) / len(lista)
valores = [2, 2]
print(media_de_uma_lista(valores))