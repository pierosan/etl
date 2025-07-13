import pandas as pd

def tranformacion(df_ubicacion, df_dispositivo):
    print("Transformando datos de ubicacion...")
    df_dispositivo_copia = df_dispositivo.copy()
    # se ordena la tabla dispositivos y se selecciona lo principal
    df_dispositivo_copia = df_dispositivo_copia[['id', 'descripcion']] 
    # se renombra la columna 
    df_dispositivo_copia.rename(columns={'id': 'id_dispositivo', 'descripcion': 'nombre_descripcion'}, inplace=True)

    # crea una nueva columna 'id' de 1 a N
    df_ubicacion['id'] = range(1, len(df_ubicacion) + 1) 
    # se renombra
    df_ubicacion.rename(columns={'dispositivo': 'nombre_descripcion_fk'}, inplace=True)
    # se ordena
    df_ubicacion = df_ubicacion[['id', 'nombre_descripcion_fk', 'timestamp', 'latitud', 'longitud']]

    df_ubicacion = pd.merge(
        df_ubicacion,
        df_dispositivo_copia,
        left_on='nombre_descripcion_fk', # Columna id_usuario del CSV de inactividad
        right_on='nombre_descripcion', # Columna de usuarios que contiene el ID de origen
        how='left' # Usamos left join para mantener todas las filas de fact_inactividad
    )

    df_ubicacion = df_ubicacion.dropna(subset=['id_dispositivo'])

    df_ubicacion['id_dispositivo'] = df_ubicacion['id_dispositivo'].astype('Int64')

    # 4. Convertir 'hora_inactividad' a formato datetime
    df_ubicacion['timestamp'] = pd.to_datetime(df_ubicacion['timestamp'])

    df_ubicacion['timestamp'] = df_ubicacion['timestamp'].dt.tz_convert('Etc/GMT+5')

    # Eliminar los microsegundos, segundos y la zona horaria
    df_ubicacion['timestamp'] = df_ubicacion['timestamp'].dt.floor('min')

    # Seleccionar solo las columnas deseadas para fact_inactividad
    df_ubicacion = df_ubicacion[['id', 'id_dispositivo', 'timestamp', 'latitud', 'longitud']]

    print(f"Datos de ubicacion transformados")

    return df_ubicacion