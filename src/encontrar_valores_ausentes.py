from typing import List

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    """Função que recebe uma lista de inteiros e retorna uma lista com os valores ausentes.
    
    Args:
        lista: Uma lista de inteiros.
    
    Returns:
        Uma lista de inteiros.
    """
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))