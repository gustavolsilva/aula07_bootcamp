# Para criar uma função em python, você usa a keyword def, seguida de um nome de função, parênteses() contendo 0 ou mais parâmetros e dois pontos:.
# O bloco de código identado que segue é o corpo da função.

# def minha_funcao():
#     return "Hello World"

#print("Esse e o meu print") # Na excução é bem simples.

# Imaginando uma calculadora

valor_1 = 4
valor_2 = 6

# valor_3 = valor_1 + valor_2

valor_4 = 50
valor_5 = 30

valor_8 = 0
# valor_6 = valor_4 + valor_5

def soma(valor_1_para_somar: float, valor_2_para_somar: float = 10) -> float:
    """
    Uma função simples de soma de valores do tipo float que retorna float
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma

# assim
#soma(valor_1, valor_2)

# ou assim
valor_3 = soma(valor_1_para_somar=valor_1, valor_2_para_somar=valor_2)
valor_6 = soma(valor_4, valor_5)
valor_7 = soma(valor_8) # 10
valor_10 = soma(0, 0) # 0

print(valor_3)
print(valor_6)
print(valor_7)
print(valor_10)