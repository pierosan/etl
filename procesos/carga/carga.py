from db import db_mysql
from . import dim_usuario_carga, dim_dispositivo_carga, fact_inactividad_carga, fact_reserva_carga, fact_sesion_carga, fact_ubicacion_gps_carga

def borrar_tablas():
    print("Borrando tablas...")
    db, cursor = db_mysql.iniciar_conexion()
    tablas = ['fact_ubicacion_gps', 'fact_sesion', 'fact_reserva', 'fact_inactividad', 'dim_dispositivo', 'dim_usuario']
    for tab in tablas:
        try:
            print(f"Borrando {tab}...")
            cursor.execute(f"DROP TABLE {tab};")
            db.commit()
            print(f"Tabla {tab} borrada")
        except :
            print(f"La tabla {tab} no existe")
    db_mysql.finalizar_conexion(db, cursor)
    print("Todas las tablas borradas")

def crear_tablas():
    print("\nCreando tablas...")
    sql = open("sql/tablas.sql", "r")
    texto_sql = sql.read()
    sentencias_sql = texto_sql.split(";")
    db, cursor = db_mysql.iniciar_conexion()
    for sentencia in sentencias_sql:
        cursor.execute(sentencia)
        db.commit()
    db_mysql.finalizar_conexion(db, cursor)
    print("Todas las tablas han sido creadas")

def iniciar(df_usuario, df_dispositivo, df_inactividad, df_reserva, df_sesion, df_ubicacion):
    print("\nCargando datos a la base de datos")
    
    db, cursor = db_mysql.iniciar_conexion()
    dim_usuario_carga.cargar(df_usuario, db, cursor)
    dim_dispositivo_carga.cargar(df_dispositivo, db, cursor)
    fact_inactividad_carga.cargar(df_inactividad, db, cursor)
    fact_reserva_carga.cargar(df_reserva, db, cursor)
    fact_sesion_carga.cargar(df_sesion, db, cursor)
    fact_ubicacion_gps_carga.cargar(df_ubicacion, db, cursor)
    db_mysql.finalizar_conexion(db, cursor)

    print("\nProceso de carga la base de datos completado.")
