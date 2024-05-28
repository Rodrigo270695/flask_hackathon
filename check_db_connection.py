import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def check_database_connection():

    database_url = os.getenv('DATABASE_URL')
    try:

        engine = create_engine(database_url)
        with engine.connect():
            print('Conexión exitosa a la base de datos')
    except Exception as e:
            print('Error de conexión a la base de datos:', e)
        
        
        