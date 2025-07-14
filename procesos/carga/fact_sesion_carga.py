from mysql.connector import Error

def cargar(df_sesion, db, cursor):
    print("Cargando fact_sesion a la base de datos")
    total = len(df_sesion)
    try:
        for index, fila in df_sesion.iterrows():
            cursor.execute("""
                INSERT INTO fact_sesion (id, id_usuario, tipo_cierre, timestamp)
                VALUES (%s, %s, %s, %s)
            """, (
                fila['id'],
                fila['id_usuario'],
                fila['tipo_cierre'],
                fila['timestamp'].to_pydatetime()
            ))
            print(f"[{index+1}/{total}] Subiendo...")
        db.commit()
        print("datos insertados en fact_sesion correctamente")
    except Error as e:
        print(f"Error al ejecutar consulta a la base de datos: {e}")