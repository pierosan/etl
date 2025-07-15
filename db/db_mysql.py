import mysql.connector
from mysql.connector import Error
from encriptado import desencriptar
import os

# Define tus credenciales de la base de datos (pueden venir de un archivo de configuración, variables de entorno, etc.)
db_host_cifrada = "f9e664602a0afaa8f31072e60980bd462ee9eb9d6ce5408c111719f9805d814e"
db_usuario_cifrada = "f9e664602a"
db_contrasena_cifrada = "f9eac7c6c756d6aa0aa2"

def iniciar_conexion():
    db = None
    cursor = None
    try:
        db_host = desencriptar.descifrar_texto(db_host_cifrada)
        db_usuario = desencriptar.descifrar_texto(db_usuario_cifrada)
        db_contrasena =desencriptar.descifrar_texto(db_contrasena_cifrada)
        print("\nConectandose a la base de datos fob_guard...")
        
        db = mysql.connector.connect(
            host=db_host,
            user=db_usuario,
            passwd=db_contrasena,
            database="fob_guard"
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
