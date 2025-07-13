import pandas as pd

def tranformacion(df_dispositivo, df_usuario):
    print("Transformando datos de dispositivo...")

    df_usuario_copia = df_usuario.copy()
    # se ordena la tabla usuarios y se selecciona lo principal
    df_usuario_copia = df_usuario_copia[['id', 'nombre']] 
    # se renombra la columna 
    df_usuario_copia.rename(columns={'id': 'id_usuario', 'nombre': 'nombre_usuario'}, inplace=True)

    # remplaza id por id_origen para mantener las referencias del id original 
    df_dispositivo = df_dispositivo.rename(columns={'id': 'id_origen', 'nfcId': 'id_nfc', 'id_dispositivo': 'num_dispositivo'})

    # generar id secuenciales de 1 a n
    df_dispositivo.insert(0, 'id', range(1, 1 + len(df_dispositivo)))

    df_dispositivo = pd.merge(
        df_dispositivo,
        df_usuario_copia,
        left_on='usuario_asignado', # Columna id_usuario del CSV de inactividad
        right_on='nombre_usuario', # Columna de usuarios que contiene el ID de origen
        how='left' # Usamos left join para mantener todas las filas de fact_inactividad
    )

    # reordenar las columnas 
    df_dispositivo = df_dispositivo[['id', 'num_dispositivo', 'descripcion', 'ubicacion', 'id_nfc', 'estado', 'id_usuario', 'fecha_registro', 'id_origen']]

    # transforma dni de texto a entero
    df_dispositivo['num_dispositivo'] = df_dispositivo['num_dispositivo'].astype(int)

    df_dispositivo['id_usuario'] = df_dispositivo['id_usuario'].astype('Int64')

    # transforma la fecha a formato datetime
    df_dispositivo['fecha_registro'] = pd.to_datetime(df_dispositivo['fecha_registro'])

    df_dispositivo['fecha_registro'] = df_dispositivo['fecha_registro'].dt.tz_convert('Etc/GMT+5')

    # Eliminar los microsegundos, segundos y la zona horaria
    df_dispositivo['fecha_registro'] = df_dispositivo['fecha_registro'].dt.floor('min')

    print(f"Datos de dispositivo transformados")

    return df_dispositivo

