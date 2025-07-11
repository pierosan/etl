import mysql.connector
from mysql.connector import Error

def conexion(host_name, user_name, user_password):
    db = None
    try:
        db = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
        )
        if db.is_connected():
            print(f"Conexión exitosa a la base de datos ")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return db

def cerrar_conexion(db):
    if db:
        db.close()
        print("Conexión a la base de datos cerrada.")
