from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    def __init__(self):
        # Inicializa a string de conexão
        self.db_uri = 'postgresql+psycopg2://myuser:mypassword@localhost:5432/mydb'
        # Cria o mecanismo de conexão
        self.engine = create_engine(self.db_uri)
        # Cria a classe de sessão
        self.Session = sessionmaker(bind=self.engine)

    def get_db_session(self):
        """Retorna uma nova sessão do banco de dados."""
        return self.Session()
