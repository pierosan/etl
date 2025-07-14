from mysql.connector import Error

def cargar(df_usuario, db, cursor):
    print("Cargando dim_usuarios a la base de datos")
    total = len(df_usuario)
    try:
        for index, fila in df_usuario.iterrows():
            cursor.execute("""
                INSERT INTO dim_usuario (id, nombre, dni, area, empresa, fecha_creacion)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                fila['id'],
                fila['nombre'],
                fila['dni'],
                fila['area'],
                fila['empresa'],
                fila['fecha_creacion'].to_pydatetime()
            ))
            print(f"[{index+1}/{total}] Subiendo...")
        db.commit()
        print("datos insertados en dim_usuarios correctamente")
    except Error as e:
        print(f"Error al ejecutar consulta a la base de datos: {e}")
    