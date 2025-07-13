import pandas as pd

def tranformacion(df_inactividad, df_usuario):
    print("Transformando datos de inactividad...")
    df_usuario_copia = df_usuario.copy()
    # se ordena la tabla usuarios y se selecciona lo principal
    df_usuario_copia = df_usuario_copia[['id', 'id_origen']] 
    # se renombra la columna 
    df_usuario_copia.rename(columns={'id': 'id_usuario'}, inplace=True)

    # crea una nueva columna 'id' de 1 a N
    df_inactividad['id'] = range(1, len(df_inactividad) + 1) 
    # renombra la columna 'usuario_id' a 'id_origen_usuario'
    df_inactividad.rename(columns={'usuario_id': 'id_origen_usuario'}, inplace=True)

    # une 'df_inactividad' con 'df_usuarios' en 'df_inactividad'
    df_inactividad = pd.merge(
        df_inactividad,
        df_usuario_copia,
        left_on='id_origen_usuario', # Columna id_usuario del CSV de inactividad
        right_on='id_origen', # Columna de usuarios que contiene el ID de origen
        how='left' # Usamos left join para mantener todas las filas de fact_inactividad
    )

    # 4. Convertir 'hora_inactividad' a formato datetime
    df_inactividad['hora_inactividad'] = pd.to_datetime(df_inactividad['hora_inactividad'])

    df_inactividad['hora_inactividad'] = df_inactividad['hora_inactividad'].dt.tz_localize('UTC')

    df_inactividad['hora_inactividad'] = df_inactividad['hora_inactividad'].dt.tz_convert('Etc/GMT+5')

    # Eliminar los microsegundos, segundos y la zona horaria
    df_inactividad['hora_inactividad'] = df_inactividad['hora_inactividad'].dt.floor('min')

    # Seleccionar solo las columnas deseadas para fact_inactividad
    df_inactividad = df_inactividad[['id', 'id_usuario', 'hora_inactividad']]

    print(f"Datos de inactividad transformados")

    return df_inactividad
