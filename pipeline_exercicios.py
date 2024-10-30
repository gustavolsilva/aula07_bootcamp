from src.media_valores_uma_lista import calcular_media
from src.filtrar_dados_acima_de_um_limite import filtrar_acima_de
from src.contar_valores_unicos_uma_lista import contar_valores_unicos
from src.converter_celsius_para_fahrenheit_em_lista import celsius_para_fahrenheit
from src.calcular_desvio_padrao_de_lista import calcular_desvio_padrao
from src.encontrar_valores_ausentes import encontrar_valores_ausentes

lista_de_valores: list = [4.5, 2.4, 3.14, 4.8, 5.2]
limite: float = 4.0
lista_repetidas: list = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]
lista_temperaturas: list = [20.0, 21.0, 22.0, 23.0, 24.0, 25.0]
lista_de_sequencia: list = [1,2,4,6,8,10]

media = calcular_media(lista_de_valores)
lista_limitada = filtrar_acima_de(lista_de_valores, limite)
lista_valor_unico = contar_valores_unicos(lista_repetidas)
lista_fahrenheit = celsius_para_fahrenheit(lista_temperaturas)
desvio_padrao = calcular_desvio_padrao(lista_de_valores)
lista_ausentes= encontrar_valores_ausentes(lista_de_sequencia)

print(f"Resp. Exercicio1 - A media dos valores da lista e: {media:.2f}")
print(f"Resp. Exercicio2 - A lista limitada e: {lista_limitada}")
print(f"Resp. Exercicio3 - A lista de valores unicos e: {lista_valor_unico}")
print(f"Resp. Exercicio4 - A lista de temperaturas em Fahrenheit e: {lista_fahrenheit}")
print(f"Resp. Exercicio5 - O desvio padrao dos valores da lista e: {desvio_padrao:.2f}")
print(f"Resp. Exercicio6 - A lista de ausencia e: {lista_ausentes}")