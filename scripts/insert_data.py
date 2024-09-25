import pandas as pd
from sqlalchemy import text
from scripts.connect_db import DatabaseManager


def insert_data_from_excel(file_path):
    # Lê os dados das planilhas
    person_df = pd.read_excel(file_path, sheet_name='Pessoa')
    car_df = pd.read_excel(file_path, sheet_name='Carro')
    driver_df = pd.read_excel(file_path, sheet_name='Motorista')

    # Cria uma instância do DatabaseManager
    db_manager = DatabaseManager()
    session = db_manager.get_db_session()

    try:
        # Inserindo os dados da tabela Person
        for _, row in person_df.iterrows():
            session.execute(
                text(
                    """
                    INSERT INTO person (cpf, name, age, cnh)
                    VALUES (:cpf, :name, :age, :cnh)
                    """
                ),
                {'cpf': str(row['cpf']), 'name': row['nome'], 'age': row['idade'], 'cnh': row['cnh']}
            )

        # Inserindo os dados da tabela Car
        for _, row in car_df.iterrows():
            session.execute(
                text(
                    """
                    INSERT INTO car (plate, model, year)
                    VALUES (:plate, :model, :year)
                    """
                ),
                {'plate': row['placa'], 'model': row['modelo'], 'year': row['ano']}
            )

        # Inserindo os dados da tabela Driver
        for _, row in driver_df.iterrows():
            session.execute(
                text(
                    """
                    INSERT INTO driver (person_id, car_id)
                    VALUES (
                        (SELECT id FROM person WHERE cpf = :person_cpf),
                        (SELECT id FROM car WHERE plate = :car_plate)
                    )
                    """
                ),
                {'person_cpf': str(row['pessoa_cpf']), 'car_plate': row['carro_placa']}
            )

        # Commit as transações
        session.commit()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        session.rollback()  # Reverte as alterações em caso de erro

    finally:
        session.close()  # Fecha a sessão


if __name__ == "__main__":
    file_path = r'../file_example/tabelas_dados.xlsx'  # Caminho do arquivo Excel
    insert_data_from_excel(file_path)
