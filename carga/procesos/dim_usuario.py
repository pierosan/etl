import sys
sys.path.append('/home/user/etl')
import pandas as pd
from db.db import iniciar_conexion
import mysql.connector
from mysql.connector import Error

usuarios_csv = '../../transformacion/resultados/dim_usuario.csv'
df_usuarios = pd.read_csv(usuarios_csv)

db = iniciar_conexion()

cursor = db.cursor()
cursor.execute("USE fob_guard;")

try:
    for _, fila in df_usuarios.iterrows():
        cursor.execute("""
            INSERT INTO dim_usuario (id, nombre, dni, area, empresa, fecha_creacion)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            fila['id'],
            fila['nombre'],
            fila['dni'],
            fila['area'],
            fila['empresa'],
            fila['fecha_creacion']
        ))
    db.commit()
    print("datos insertados en dim_usuarios correctamente")
except Error as e:
    print(f"Error al ejecutar consulta a la base de datos: {e}")