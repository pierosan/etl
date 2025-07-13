import pandas as pd

def tranformacion(df_sesion, df_usuario):
    print("Transformando datos de la sesion...")
    df_usuario_copia = df_usuario.copy()
    # se ordena la tabla usuarios y se selecciona lo principal
    df_usuario_copia = df_usuario_copia[['id', 'id_origen']] 
    # se renombra la columna 
    df_usuario_copia.rename(columns={'id': 'id_usuario', 'id_origen': 'id_origen_usuario'}, inplace=True)

    # crea una nueva columna 'id' de 1 a N
    df_sesion['id'] = range(1, len(df_sesion) + 1) 
    # se renombra
    df_sesion.rename(columns={'usuario_id':'id_origen_usuario_fk'}, inplace=True)
    # se ordena
    df_sesion = df_sesion[['id', 'id_origen_usuario_fk', 'tipo_cierre', 'timestamp']]

    # une
    df_sesion = pd.merge(
        df_sesion,
        df_usuario_copia,
        left_on='id_origen_usuario_fk', # Columna id_usuario del CSV de inactividad
        right_on='id_origen_usuario', # Columna de usuarios que contiene el ID de origen
        how='left' # Usamos left join para mantener todas las filas de fact_inactividad
    )

    df_sesion['timestamp'] = pd.to_datetime(df_sesion['timestamp'])

    df_sesion['timestamp'] = df_sesion['timestamp'].dt.tz_convert('Etc/GMT+5')

    # Eliminar los microsegundos, segundos y la zona horaria
    df_sesion['timestamp'] = df_sesion['timestamp'].dt.floor('min')

    df_sesion = df_sesion[['id', 'id_usuario', 'tipo_cierre', 'timestamp']]

    print(f"Datos de sesion transformados")

    return df_sesion