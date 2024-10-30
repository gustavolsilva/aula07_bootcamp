from typing import List

def calcular_desvio_padrao(valores: List[float]) -> float:
    """
    Funcao que calcula o desvio padrao de uma lista de valores
    """
    media = sum(valores) / len(valores)
    variancia = sum((valor - media) ** 2 for valor in valores) / len(valores)
    return variancia ** 0.5