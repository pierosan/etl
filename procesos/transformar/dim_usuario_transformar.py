import pandas as pd

def tranformacion(df_usuario):
    print("Transformando datos de usuario...")
    
    # remplaza id por id_origen para mantener las referencias del id original 
    df_usuario = df_usuario.rename(columns={'id': 'id_origen'})

    # renombrar 'fechaCreacion' a 'fecha_creacion'
    df_usuario = df_usuario.rename(columns={'fechaCreacion': 'fecha_creacion'})

    # generar id secuenciales de 1 a n
    df_usuario.insert(0, 'id', range(1, 1 + len(df_usuario)))

    # reordenar las columnas 
    df_usuario = df_usuario[['id', 'nombre', 'dni', 'area', 'empresa', 'fecha_creacion', 'id_origen']]

    # transforma dni de texto a entero
    df_usuario['dni'] = df_usuario['dni'].astype(int)

    # transforma la fecha a formato datetime
    df_usuario['fecha_creacion'] = pd.to_datetime(df_usuario['fecha_creacion'])

    df_usuario['fecha_creacion'] = df_usuario['fecha_creacion'].dt.tz_convert('Etc/GMT+5')

    # Eliminar los microsegundos, segundos y la zona horaria
    df_usuario['fecha_creacion'] = df_usuario['fecha_creacion'].dt.floor('min')

    print("Datos de usuarios transformados")

    return df_usuario
