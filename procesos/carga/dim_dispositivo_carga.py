import pandas as pd
from mysql.connector import Error

def cargar(df_dispositivo, db, cursor):
    print("Cargando dim_dispositivo a la base de datos")
    total = len(df_dispositivo)
    try:
        for index, fila in df_dispositivo.iterrows():
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
                fila['fecha_registro'].to_pydatetime()
            ))
            print(f"[{index+1}/{total}] Subiendo...")
        db.commit()
        print("datos insertados en dim_dispositivo correctamente")
    except Error as e:
        print(f"Error al ejecutar consulta a la base de datos: {e}")