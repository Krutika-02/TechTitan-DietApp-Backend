import os
import toml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from psycopg2 import OperationalError
from models import user_management

class DBResourceManager():

    def __init__(self, db_key: str = None) -> None:
        # DB Config
        config_path = os.path.abspath("config.toml")
        config = toml.load(config_path)

        self.db_key = db_key
        self.database_url = config['postgresql'].get(db_key)
        if not self.database_url:
            raise ValueError(f"Database key '{db_key}' not found in configuration.")

        self.engine = create_engine(self.database_url)
        self.Base = self.get_base_for_db(db_key)  # Initialize Base based on db_key
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)


    def get_base_for_db(self, db_key):
        if db_key == 'diet_management':
            return user_management.Base
        raise ValueError(f"Unsupported database key: {db_key}")

    def connect(self):
        try:
            session = self.Session()
            return session
        except OperationalError as e:
            print("Error connecting to the database:", e)
            return None

    def close(self):
        if self.engine:
            self.engine.dispose()
            print("Database connection closed")
