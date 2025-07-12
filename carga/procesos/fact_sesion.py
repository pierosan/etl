import sys
sys.path.append('/home/user/etl')
import pandas as pd
from db.db import iniciar_conexion
import mysql.connector
from mysql.connector import Error

sesiones_csv = '../../transformacion/resultados/fact_sesiones.csv'
df_sesion = pd.read_csv(sesiones_csv)

db = iniciar_conexion()

cursor = db.cursor()
cursor.execute("USE fob_guard;")

try:
    for _, fila in df_sesion.iterrows():
        cursor.execute("""
            INSERT INTO fact_sesion (id, id_usuario, tipo_cierre, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (
            fila['id'],
            fila['id_usuario'],
            fila['tipo_cierre'],
            fila['timestamp']
        ))
    db.commit()
    print("datos insertados en fact_sesion correctamente")
except Error as e:
    print(f"Error al ejecutar consulta a la base de datos: {e}")