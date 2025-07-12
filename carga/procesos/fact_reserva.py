import sys
sys.path.append('/home/user/etl')
import pandas as pd
from db.db import iniciar_conexion
import mysql.connector
from mysql.connector import Error

reserva_csv = '../../transformacion/resultados/fact_reserva.csv'
df_reserva = pd.read_csv(reserva_csv)

db = iniciar_conexion()

cursor = db.cursor()
cursor.execute("USE fob_guard;")

try:
    for _, fila in df_reserva.iterrows():
        cursor.execute("""
            INSERT INTO fact_reserva (id, id_dispositivo, id_usuario, fecha_reserva, motivo_reserva, tipo_movimiento, estado_dispositivo)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            fila['id'],
            fila['id_dispositivo'],
            fila['id_usuario'],
            fila['fecha_reserva'],
            fila['motivo_reserva'],
            fila['tipo_movimiento'],
            fila['estado_dispositivo']
        ))
    db.commit()
    print("datos insertados en fact_reserva correctamente")
except Error as e:
    print(f"Error al ejecutar consulta a la base de datos: {e}")