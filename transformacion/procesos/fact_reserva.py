import pandas as pd

# --- Carga de datos ---
usuarios_csv = '../resultados/dim_usuario.csv'
df_usuarios = pd.read_csv(usuarios_csv)

dispositivos_csv = '../resultados/dim_dispositivo.csv'
df_dispositivos = pd.read_csv(dispositivos_csv)

reservas_csv = '../../extraccion/colecciones/reservas.csv'
df_reservas = pd.read_csv(reservas_csv)

# se ordena la tabla usuarios y se selecciona lo principal
df_usuarios = df_usuarios[['id', 'id_origen']] 
# se renombra la columna 
df_usuarios.rename(columns={'id': 'id_usuario', 'id_origen': 'id_origen_usuario'}, inplace=True)

# se ordena la tabla dispositivos y se selecciona lo principal
df_dispositivos = df_dispositivos[['id', 'id_origen']] 
# se renombra la columna 
df_dispositivos.rename(columns={'id': 'id_dispositivo', 'id_origen': 'id_origen_dispositivo'}, inplace=True)

# crea una nueva columna 'id' de 1 a N
df_reservas['id'] = range(1, len(df_reservas) + 1) 
# se renombra
df_reservas.rename(columns={'dispositivoId': 'id_origen_dispositivo_fk', 'usuarioId': 'id_origen_usuario_fk', 'fechaReserva': 'fecha_reserva', 'motivoReserva': 'motivo_reserva', 'tipoMovimiento':'tipo_movimiento', 'estadoDispositivo':'estado_dispositivo'}, inplace=True)
# se ordena
df_reservas = df_reservas[['id', 'id_origen_dispositivo_fk', 'id_origen_usuario_fk', 'fecha_reserva', 'motivo_reserva', 'tipo_movimiento', 'estado_dispositivo']]


# une 
df_reservas = pd.merge(
    df_reservas,
    df_dispositivos,
    left_on='id_origen_dispositivo_fk', # Columna id_usuario del CSV de inactividad
    right_on='id_origen_dispositivo', # Columna de usuarios que contiene el ID de origen
    how='left' # Usamos left join para mantener todas las filas de fact_inactividad
)
df_reservas = pd.merge(
    df_reservas,
    df_usuarios,
    left_on='id_origen_usuario_fk', # Columna id_usuario del CSV de inactividad
    right_on='id_origen_usuario', # Columna de usuarios que contiene el ID de origen
    how='left' # Usamos left join para mantener todas las filas de fact_inactividad
)


# 4. Convertir 'hora_inactividad' a formato datetime
df_reservas['fecha_reserva'] = pd.to_datetime(df_reservas['fecha_reserva'])

# Seleccionar solo las columnas deseadas para fact_inactividad
df_reservas = df_reservas[['id', 'id_dispositivo', 'id_usuario', 'fecha_reserva', 'motivo_reserva', 'tipo_movimiento', 'estado_dispositivo']]


# --- Guardar el resultado ---
reserva_csv_salida = '../resultados/fact_reserva.csv'
df_reservas.to_csv(reserva_csv_salida, index=False)

print(f"Datos transformados y guardados en '{reserva_csv_salida}'")
