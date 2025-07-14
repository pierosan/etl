from db import db_mysql
from . import dim_usuario_carga, dim_dispositivo_carga, fact_inactividad_carga, fact_reserva_carga, fact_sesion_carga, fact_ubicacion_gps_carga

def borrar_tablas():
    print("\nBorrando tablas...")
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
    db, cursor = db_mysql.iniciar_conexion()
    comando_sql = """
    CREATE TABLE dim_usuario (
        id INT UNIQUE PRIMARY KEY,
        nombre VARCHAR(255),
        dni INT,
        area VARCHAR(100),
        empresa VARCHAR(100),
        fecha_creacion DATETIME,
        INDEX (nombre)
    );
    CREATE TABLE dim_dispositivo (
        id INT UNIQUE PRIMARY KEY,
        num_dispositivo INT,
        descripcion VARCHAR(50),
        ubicacion VARCHAR(50),
        id_nfc VARCHAR(50),
        estado VARCHAR(50),
        id_usuario INT,
        fecha_registro DATETIME,
        INDEX (descripcion),
        FOREIGN KEY (id_usuario) REFERENCES dim_usuario(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
        
    );
    CREATE TABLE fact_inactividad (
        id INT UNIQUE PRIMARY KEY,
        id_usuario INT,
        hora_inactividad DATETIME,
        FOREIGN KEY (id_usuario) REFERENCES dim_usuario(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );
    CREATE TABLE fact_reserva (
        id INT UNIQUE PRIMARY KEY,
        id_dispositivo INT,
        id_usuario INT,
        fecha_reserva DATETIME,
        motivo_reserva VARCHAR(255),
        tipo_movimiento VARCHAR(50),
        estado_dispositivo VARCHAR(50),
        FOREIGN KEY (id_dispositivo) REFERENCES dim_dispositivo(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE,
        FOREIGN KEY (id_usuario) REFERENCES dim_usuario(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );
    CREATE TABLE fact_sesion (
        id INT UNIQUE PRIMARY KEY,
        id_usuario INT,
        tipo_cierre VARCHAR(255),
        timestamp DATETIME,
        FOREIGN KEY (id_usuario) REFERENCES dim_usuario(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );
    CREATE TABLE fact_ubicacion_gps (
        id INT UNIQUE PRIMARY KEY,
        id_dispositivo INT,
        timestamp DATETIME,
        latitud DECIMAL(10, 7),
        longitud DECIMAL(10, 7),
        FOREIGN KEY (id_dispositivo) REFERENCES dim_dispositivo(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );
    """
    cursor.execute(comando_sql)
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
    
