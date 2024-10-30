from typing import List

def calcular_media(valores: List[float]) -> float:
    """
    Funcao que calcula a media de uma lista de valores
    """
    return sum(valores) / len(valores)