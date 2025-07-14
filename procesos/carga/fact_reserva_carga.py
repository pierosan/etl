from mysql.connector import Error

def cargar(df_reserva, db, cursor):
    print("Cargando fact_reserva a la base de datos")
    total = len(df_reserva)
    try:
        for index, fila in df_reserva.iterrows():
            cursor.execute("""
                INSERT INTO fact_reserva (id, id_dispositivo, id_usuario, fecha_reserva, motivo_reserva, tipo_movimiento, estado_dispositivo)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                fila['id'],
                fila['id_dispositivo'],
                fila['id_usuario'],
                fila['fecha_reserva'].to_pydatetime(),
                fila['motivo_reserva'],
                fila['tipo_movimiento'],
                fila['estado_dispositivo']
            ))
            print(f"[{index+1}/{total}] Subiendo...")
        db.commit()
        print("datos insertados en fact_reserva correctamente")
    except Error as e:
        print(f"Error al ejecutar consulta a la base de datos: {e}")