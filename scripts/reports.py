from sqlalchemy import text


class ReportManager:
    def __init__(self, database_manager):
        """Inicializa o ReportManager com uma instância do DatabaseManager."""
        self.database_manager = database_manager

    def report_find_driver_by_cpf(self, cpf):
        """Gera um relatório com as informações do motorista pelo CPF."""
        session = self.database_manager.get_db_session()
        try:
            # Define a consulta SQL
            query = text(""" 
                SELECT 
                    p.name AS driver_name,
                    p.cpf,
                    c.model AS car_model,
                    c.plate
                FROM person p
                JOIN driver m ON p.id = m.person_id
                JOIN car c ON m.car_id = c.id
                WHERE p.cpf = :cpf
            """)

            result = session.execute(query, {'cpf': cpf})
            resultados = result.fetchall()

            return [[row.driver_name, row.cpf, row.car_model, row.plate] for row in resultados]
        finally:
            session.close()

    def report_find_all_drivers(self):
        """Gera um relatório com todos os motoristas e seus respectivos carros."""
        session = self.database_manager.get_db_session()
        try:
            query = text(""" 
                SELECT 
                    m.id AS driver_id,
                    p.name AS driver_name,
                    p.cpf,
                    c.model AS car_model,
                    c.plate
                FROM person p
                JOIN driver m ON p.id = m.person_id
                JOIN car c ON m.car_id = c.id
            """)
            result = session.execute(query)
            resultados = result.fetchall()
            return [[row.driver_id, row.driver_name, row.cpf, row.car_model, row.plate] for row in resultados]
        finally:
            session.close()

    def report_find_person_by_name(self, name):
        """Gera um relatório com as pessoas que têm um nome correspondente."""
        session = self.database_manager.get_db_session()
        try:
            query = text(""" 
                SELECT * FROM person WHERE name ILIKE :name
            """)
            result = session.execute(query, {'name': f'%{name}%'})
            resultados = result.fetchall()
            return [[row.id, row.cpf, row.name, row.age, row.cnh] for row in resultados]
        finally:
            session.close()

    def report_find_all_people(self):
        """Gera um relatório com todas as pessoas."""
        session = self.database_manager.get_db_session()
        try:
            query = text(""" 
                SELECT * FROM person
            """)
            result = session.execute(query)
            resultados = result.fetchall()
            return [[row.id, row.cpf, row.name, row.age, row.cnh] for row in resultados]
        finally:
            session.close()

    def report_find_car_by_model(self, model):
        """Gera um relatório com os carros que têm um modelo correspondente."""
        session = self.database_manager.get_db_session()
        try:
            query = text(""" 
                SELECT * FROM car WHERE model ILIKE :model
            """)
            result = session.execute(query, {'model': f'%{model}%'})
            resultados = result.fetchall()
            return [[row.id, row.plate, row.model, row.year] for row in resultados]
        finally:
            session.close()

    def report_find_all_car(self):
        """Gera um relatório com todos os carros."""
        session = self.database_manager.get_db_session()
        try:
            query = text("""SELECT * FROM car""")
            result = session.execute(query)
            resultados = result.fetchall()
            return [[row.id, row.plate, row.model, row.year] for row in resultados]
        finally:
            session.close()


# Exemplo de uso
if __name__ == '__main__':
    from scripts.connect_db import DatabaseManager

    # Criando a instância do DatabaseManager
    db_manager = DatabaseManager()

    # Criando a instância do ReportManager passando o DatabaseManager
    report_manager = ReportManager(db_manager)

    car_model = 'Honda'

    # Exemplo de chamadas para gerar relatórios
    drivers = report_manager.report_find_all_drivers()
    print("Todos os Motoristas:", drivers)

    driver_by_cpf = report_manager.report_find_driver_by_cpf('46787766050')
    print("Motorista por CPF:", driver_by_cpf)

    people = report_manager.report_find_all_people()
    print("Todas as Pessoas:", people)

    cars = report_manager.report_find_car_by_model(car_model)
    print(f"Carros pelo modelo {car_model}:", cars)

    all_cars = report_manager.report_find_all_car()
    print("Todos os Carros:", all_cars)
