from mysql.connector import Error

def cargar(df_inactividad, db, cursor):
    print("Cargando fact_inactividad a la base de datos")
    total = len(df_inactividad)
    try:
        for index, fila in df_inactividad.iterrows():
            cursor.execute("""
                INSERT INTO fact_inactividad (id, id_usuario, hora_inactividad)
                VALUES (%s, %s, %s)
            """, (
                fila['id'],
                fila['id_usuario'],
                fila['hora_inactividad'].to_pydatetime()
            ))
            print(f"[{index+1}/{total}] Subiendo...")
        db.commit()
        print("datos insertados en fact_inactividad correctamente")
    except Error as e:
        print(f"Error al ejecutar consulta a la base de datos: {e}")