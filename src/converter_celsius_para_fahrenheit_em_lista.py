from typing import List

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    """
    Funcao que converte temperaturas de Celsius para Fahrenheit
    """
    return [temperatura * 9/5 + 32 for temperatura in temperaturas_celsius]