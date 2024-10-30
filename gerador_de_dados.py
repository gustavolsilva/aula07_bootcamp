import csv
import random
import datetime

num_linhas: int = int(input("Digite o número de linhas que deseja gerar: ")) 
inicio = datetime.datetime.now()
print(f"{inicio} - Gerando {num_linhas} linhas de dados...")

def generate_fake_data(num_records, file_path):
    products = [
        "Mesa de Jantar", "Mesa de Centro", "Mesa de Escritório", "Cadeira de Escritório",
        "Cadeira de Jantar", "Cadeira de Praia", "Cadeira Gamer", "Cadeira Dobrável", "Sofá","Sofá-Cama",
        "Sofá de Canto", "Sofá 3 Lugares", "Sofá 2 Lugares", "Sofá 4 Lugares", "Guarda-Roupa", "Guarda-Roupa Casal",
        "Guarda-Roupa Solteiro", "Guarda-Roupa Infantil", "Guarda-Roupa Embutido", "Guarda-Roupa Planejado",
        "Cama Box", "Cama Box Casal", "Cama Box Solteiro", "Cama Box King Size", "Cama Box Queen Size",
        "Cama Box Baú", "Cama Box com Gavetas", "Cama Box com Cabeceira", "Cama Box com Criado-Mudo",
        "Cama Box com Baú e Gavetas", "Cama Box com Baú e Cabeceira", "Cama Box com Baú e Criado-Mudo",
        "Cama Box com Gavetas e Cabeceira", "Cama Box com Gavetas e Criado-Mudo", "Cama Box com Cabeceira e Criado-Mudo",
        "Cama Box com Baú, Gavetas e Cabeceira", "Cama Box com Baú, Gavetas e Criado-Mudo",
        "Cama Box com Baú, Cabeceira e Criado-Mudo", "Cama Box com Gavetas, Cabeceira e Criado-Mudo",
        "Computador", "Notebook", "Ultrabook", "Netbook", "Macbook", "All-in-One", "Mini PC", "Desktop",
        "Monitor", "Monitor Gamer", "Monitor Ultrawide", "Monitor Curvo", "Monitor Touchscreen", "Monitor 4K",
        "Monitor Full HD", "Monitor HD", "Monitor 144Hz", "Monitor 240Hz", "Monitor 360Hz", "Monitor 60Hz",
        "Monitor 75Hz", "Monitor 120Hz", "Monitor 165Hz", "Monitor 200Hz", "Monitor 240Hz", "Monitor 280Hz",
        "Tenis", "Camisa", "Calça", "Bermuda", "Boné", "Chapéu", "Cinto", "Relógio", "Pulseira", "Colar",
        "Brinco", "Anel", "Mochila", "Bolsa", "Carteira", "Óculos de Sol", "Óculos de Grau", "Perfume",
        "Shampoo", "Condicionador", "Sabonete", "Creme Dental", "Escova de Dente", "Fio Dental", "Desodorante",
        "Protetor Solar", "Protetor Labial", "Hidratante", "Creme Anti-Idade", "Creme Anti-Rugas", "Creme Anti-Manchas",
        "Creme Anti-Celulite", "Creme Anti-Estrias", "Creme Anti-Olheiras", "Creme Anti-Acne", "Creme Anti-Cravos",
        "Creme Anti-Espinhas", "Creme Anti-Ressecamento", "Creme Anti-Inflamação", "Creme Anti-Irritação",
        "Creme Anti-Envelhecimento", "Creme Anti-Ressecamento", "Creme Anti-Inflamação", "Creme Anti-Irritação",
        "Recipiente de Alimento", "Recipiente de Bebida", "Recipiente de Lixo", "Recipiente de Limpeza",
        "Recipiente de Higiene", "Recipiente de Papel", "Recipiente de Plástico", "Recipiente de Vidro"
    ]
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["produto", "price", "entregue"])
        
        for _ in range(num_records):
            product = random.choice(products)
            price = round(random.uniform(50.0, 1000.0), 2)
            delivered = random.choice([True, False])
            writer.writerow([product, price, delivered])

# Exemplo de uso
generate_fake_data(num_records=num_linhas, file_path='/home/gustavo/Projects/Python/aula07_bootcamp/vendas.csv')
fim = datetime.datetime.now()
print(f"{fim} - {num_linhas} linhas geradas em {fim - inicio} segundos.")