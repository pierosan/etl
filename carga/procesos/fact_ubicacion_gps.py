import sys
sys.path.append('/home/user/etl')
import pandas as pd
from db.db import iniciar_conexion
import mysql.connector
from mysql.connector import Error

ubicaciones_csv = '../../transformacion/resultados/fact_ubicacion_gps.csv'
df_ubicaciones = pd.read_csv(ubicaciones_csv)

db = iniciar_conexion()

cursor = db.cursor()
cursor.execute("USE fob_guard;")

try:
    for _, fila in df_ubicaciones.iterrows():
        cursor.execute("""
            INSERT INTO fact_ubicacion_gps (id, id_dispositivo, timestamp, latitud, longitud)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            fila['id'],
            fila['id_dispositivo'],
            fila['timestamp'],
            fila['latitud'],
            fila['longitud'],
        ))
    db.commit()
    print("datos insertados en fact_ubicacion_gps correctamente")
except Error as e:
    print(f"Error al ejecutar consulta a la base de datos: {e}")