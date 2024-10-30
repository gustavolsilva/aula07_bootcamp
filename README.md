# aula07_bootcamp

## Funções

Imagine uma situação de projeto: <br>
Você precisa fazer uma ETL (Extract, Transformation, Load).
Existem três módulos:
> Excel.py <br>
> API.py <br>
> SQL.py

Dentro de cada um deles, tem seus respectivos códigos com a parte de Extração (Extract), Transformação (Transformation) e Carga (Load). Inicialmente a carga acontecia em Postgres, tornou-se Duckdb. 
Logo, você terá que alterar todos os códigos e sua respectiva saída de Postgres para Duckdb.

Esta situação seria trabalhosa, mas conseguira fazer. Agora imagine que você teria 30 ou 60 ou até 600 códigos para fazer esta mesma alteração.

A função ajudará neste termo, pois ao invés de fazer um código de load para cada módulo. Podemos criar uma função de load dentro do arquivo ```etl.py``` e invocar em cada uma dos módulos do nosso exemplo.

Função é sinônimo de eficiência e maturidade de software.

## Instrução para execução do Projeto:

Execute o ```gerador_de_dados.py```
```
python gerador_de_dados.py
```
Informe o número de linhas para a geração do arquivo de vendas.csv

Após, execute o arquivo ```main.py```

```
python main.py
```

## Instrução para execução dos exercicios de Função
Execute o arqauivo ```pipeline_exercicios.py```
```
python pipeline_exercicios.py
```