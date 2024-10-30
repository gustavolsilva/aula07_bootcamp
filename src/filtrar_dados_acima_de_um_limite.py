from typing import List

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    """
    Funcao que filtra valores acima de um determinado limite
    """
    resultado: list = []
    resultado = [valor for valor in valores if valor > limite]
    return resultado