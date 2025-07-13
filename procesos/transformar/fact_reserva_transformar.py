import pandas as pd

def tranformacion(df_reserva, df_usuario, df_dispositivo):
    print("Transformando datos de reserva...")
    df_usuario_copia = df_usuario.copy()
    df_dispositivo_copia = df_dispositivo.copy()
    # se ordena la tabla usuarios y se selecciona lo principal
    df_usuario_copia = df_usuario_copia[['id', 'id_origen']] 
    # se renombra la columna 
    df_usuario_copia.rename(columns={'id': 'id_usuario', 'id_origen': 'id_origen_usuario'}, inplace=True)

    # se ordena la tabla dispositivos y se selecciona lo principal
    df_dispositivo_copia = df_dispositivo_copia[['id', 'id_origen']] 
    # se renombra la columna 
    df_dispositivo_copia.rename(columns={'id': 'id_dispositivo', 'id_origen': 'id_origen_dispositivo'}, inplace=True)

    # crea una nueva columna 'id' de 1 a N
    df_reserva['id'] = range(1, len(df_reserva) + 1) 
    # se renombra
    df_reserva.rename(columns={'dispositivoId': 'id_origen_dispositivo_fk', 'usuarioId': 'id_origen_usuario_fk', 'fechaReserva': 'fecha_reserva', 'motivoReserva': 'motivo_reserva', 'tipoMovimiento':'tipo_movimiento', 'estadoDispositivo':'estado_dispositivo'}, inplace=True)
    # se ordena
    df_reserva = df_reserva[['id', 'id_origen_dispositivo_fk', 'id_origen_usuario_fk', 'fecha_reserva', 'motivo_reserva', 'tipo_movimiento', 'estado_dispositivo']]

    # une 
    df_reserva = pd.merge(
        df_reserva,
        df_dispositivo_copia,
        left_on='id_origen_dispositivo_fk', # Columna id_usuario del CSV de inactividad
        right_on='id_origen_dispositivo', # Columna de usuarios que contiene el ID de origen
        how='left' # Usamos left join para mantener todas las filas de fact_inactividad
    )
    df_reserva = pd.merge(
        df_reserva,
        df_usuario_copia,
        left_on='id_origen_usuario_fk', # Columna id_usuario del CSV de inactividad
        right_on='id_origen_usuario', # Columna de usuarios que contiene el ID de origen
        how='left' # Usamos left join para mantener todas las filas de fact_inactividad
    )

    # 4. Convertir 'hora_inactividad' a formato datetime
    df_reserva['fecha_reserva'] = pd.to_datetime(df_reserva['fecha_reserva'])

    df_reserva['fecha_reserva'] = df_reserva['fecha_reserva'].dt.tz_convert('Etc/GMT+5')

    # Eliminar los microsegundos, segundos y la zona horaria
    df_reserva['fecha_reserva'] = df_reserva['fecha_reserva'].dt.floor('min')

    # Seleccionar solo las columnas deseadas para fact_inactividad
    df_reserva = df_reserva[['id', 'id_dispositivo', 'id_usuario', 'fecha_reserva', 'motivo_reserva', 'tipo_movimiento', 'estado_dispositivo']]

    print(f"Datos de reserva transformados")

    return df_reserva
