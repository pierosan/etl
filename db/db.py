import mysql.connector
from mysql.connector import Error
import os
import dotenv

dotenv.load_dotenv()

# Define tus credenciales de la base de datos (pueden venir de un archivo de configuración, variables de entorno, etc.)
DB_HOST = os.getenv('DB_HOST')
DB_USUARIO = os.getenv('DB_USUARIO')
DB_CONTRASENA = os.getenv('DB_CONTRASENA')

def iniciar_conexion():
    db = None
    try:
        db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USUARIO,
            passwd=DB_CONTRASENA,
        )
        if db.is_connected():
            print(f"Conexión exitosa a la base de datos ")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return db