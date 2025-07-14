import mysql.connector
from mysql.connector import Error
import os

# Define tus credenciales de la base de datos (pueden venir de un archivo de configuración, variables de entorno, etc.)
DB_HOST = os.getenv('DB_HOST')
DB_USUARIO = os.getenv('DB_USUARIO')
DB_CONTRASENA = os.getenv('DB_CONTRASENA')
DB_NOMBRE = os.getenv('DB_NOMBRE')

def iniciar_conexion():
    db = None
    cursor = None
    try:
        print("\nConectandose a la base de datos fob_guard...")
        db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USUARIO,
            passwd=DB_CONTRASENA,
            database=DB_NOMBRE
        )
        if db.is_connected():
            print("Conexión exitosa a la base de datos fob_guard\n")
            cursor = db.cursor()
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return db, cursor

def finalizar_conexion(db, cursor):
    print("\nCerrando conexion a la base de datos...")
    cursor.close()
    db.close()
    print("Conexion a la base de datos cerrada\n")
