import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Crear la URL de conexión a la base de datos
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)

# Intentar conectarse
with engine.connect() as connection:
    # Crear las tablas si no existen
    engine.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INT NOT NULL,
            name VARCHAR(255) NOT NULL,
            PRIMARY KEY(publisher_id)
        );

        -- Resto de las sentencias CREATE TABLE IF NOT EXISTS
    """)

    # Insertar datos
    engine.execute("""
        -- Sentencias INSERT INTO ...
    """)

# Utilizar pandas para imprimir una de las tablas como un DataFrame
result_dataFrame = pd.read_sql("SELECT * FROM publishers;", engine)
print(result_dataFrame)
