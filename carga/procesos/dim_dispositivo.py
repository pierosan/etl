import sys
sys.path.append('/home/user/etl')
import pandas as pd
from db.db import iniciar_conexion
import mysql.connector
from mysql.connector import Error

dispositivos_csv = '../../transformacion/resultados/dim_dispositivo.csv'
df_dispositivos = pd.read_csv(dispositivos_csv)

db = iniciar_conexion()

cursor = db.cursor()
cursor.execute("USE fob_guard;")

try:
    for _, fila in df_dispositivos.iterrows():
        cursor.execute("""
            INSERT INTO dim_dispositivo (id, num_dispositivo, descripcion, ubicacion, id_nfc, estado, id_usuario, fecha_registro)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            fila['id'],
            fila['num_dispositivo'],
            fila['descripcion'],
            fila['ubicacion'],
            fila['id_nfc'],
            fila['estado'],
            fila['id_usuario'] if pd.notna(fila['id_usuario']) else None,
            fila['fecha_registro']
        ))
    db.commit()
    print("datos insertados en dim_dispositivo correctamente")
except Error as e:
    print(f"Error al ejecutar consulta a la base de datos: {e}")