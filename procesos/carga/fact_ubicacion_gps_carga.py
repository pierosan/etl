from mysql.connector import Error

def cargar(df_ubicacione, db, cursor):
    print("Cargando fact_ubicaciones_gps a la base de datos")
    index = 1
    total = len(df_ubicacione)
    try:
        for _, fila in df_ubicacione.iterrows():
            cursor.execute("""
                INSERT INTO fact_ubicacion_gps (id, id_dispositivo, timestamp, latitud, longitud)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                fila['id'],
                fila['id_dispositivo'],
                fila['timestamp'].to_pydatetime(),
                fila['latitud'],
                fila['longitud'],
            ))
            print(f"[{index}/{total}] Subiendo...")
            index += 1
        db.commit()
        print("datos insertados en fact_ubicacion_gps correctamente")
    except Error as e:
        print(f"Error al ejecutar consulta a la base de datos: {e}")