# Databricks Data Integration

Este projeto simula um banco de dados PostgreSQL usando Docker. O banco de dados possui três tabelas: `pessoa`, `carro` e `motorista`, com alguns dados de exemplo.

## Objetivo:
- **ETL Simulation with Pandas and PostgreSQL**: Destaca o processo de extração, transformação e carregamento de dados
- **DB Seeder with Pandas and PostgreSQL in Docker**: Reflete o foco em popular o banco de dados a partir de arquivos Excel usando Pandas.
- **Dockerized Database with Pandas ETL**: Combina Docker, Pandas e o conceito de ETL.

## Pré-requisitos
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org)

## Como rodar o projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/LucasDiasTavares/DatabricksDataIntegration.git
    cd mini-projeto-docker-postgres
    ```

2. Execute o Docker Compose:
    ```bash
    docker-compose up
    ```

3. Acesse o banco de dados PostgreSQL no localhost:
    - **Host:** `localhost`
    - **Porta:** `5432`
    - **Usuário:** `myuser`
    - **Senha:** `mypassword`
    - **Banco de dados:** `mydb`

Você pode acessar o banco de dados via um cliente PostgreSQL, como o [pgAdmin](https://www.pgadmin.org/) ou a linha de comando:
```bash
psql -h localhost -U myuser -d mydb
```

## Estrutura do banco de dados
- Tabela pessoa: armazena informações sobre as pessoas.
- Tabela carro: armazena informações sobre os carros.
- Tabela motorista: relaciona uma pessoa a um carro.

## Relatórios
Na pasta scripts arquivo reports.py contém alguns exemplos de como trazer os dados para exemplificar relatórios.
- **report_find_all_people**: Buscar todas as pessoas, método que retorna todas as pessoas.
- **report_find_all_car**: Buscar todos os carros, método que retorna todos os carros.
- **report_find_all_drivers**: Buscar todos os motoristas, método que retorna todos os motoristas e seus respectivos carros.
- **report_find_person_by_name**: Buscar pessoa pelo Nome método que busca uma pessoa pelo nome.
- **report_find_driver_by_cpf**: Buscar motorista pelo CPF, método que retorna o motorista e seu respectivo carro.
- **report_find_car_by_model**: Buscar carro pelo modelo, método que busca carros pelo modelo.


