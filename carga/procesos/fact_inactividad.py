import sys
sys.path.append('/home/user/etl')
import pandas as pd
from db.db import iniciar_conexion
import mysql.connector
from mysql.connector import Error

inactividad_csv = '../../transformacion/resultados/fact_inactividad.csv'
df_inactividad = pd.read_csv(inactividad_csv)

db = iniciar_conexion()

cursor = db.cursor()
cursor.execute("USE fob_guard;")

try:
    for _, fila in df_inactividad.iterrows():
        cursor.execute("""
            INSERT INTO fact_inactividad (id, id_usuario, hora_inactividad)
            VALUES (%s, %s, %s)
        """, (
            fila['id'],
            fila['id_usuario'],
            fila['hora_inactividad']
        ))
    db.commit()
    print("datos insertados en fact_inactividad correctamente")
except Error as e:
    print(f"Error al ejecutar consulta a la base de datos: {e}")