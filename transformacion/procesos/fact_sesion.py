import pandas as pd

# --- Carga de datos ---
usuarios_csv = '../resultados/dim_usuario.csv'
df_usuarios = pd.read_csv(usuarios_csv)

sesiones_csv = '../../extraccion/colecciones/registro_sesiones.csv'
df_sesiones = pd.read_csv(sesiones_csv)

# se ordena la tabla usuarios y se selecciona lo principal
df_usuarios = df_usuarios[['id', 'id_origen']] 
# se renombra la columna 
df_usuarios.rename(columns={'id': 'id_usuario', 'id_origen': 'id_origen_usuario'}, inplace=True)

# crea una nueva columna 'id' de 1 a N
df_sesiones['id'] = range(1, len(df_sesiones) + 1) 
# se renombra
df_sesiones.rename(columns={'usuario_id':'id_origen_usuario_fk'}, inplace=True)
# se ordena
df_sesiones = df_sesiones[['id', 'id_origen_usuario_fk', 'tipo_cierre', 'timestamp']]

# une
df_sesiones = pd.merge(
    df_sesiones,
    df_usuarios,
    left_on='id_origen_usuario_fk', # Columna id_usuario del CSV de inactividad
    right_on='id_origen_usuario', # Columna de usuarios que contiene el ID de origen
    how='left' # Usamos left join para mantener todas las filas de fact_inactividad
)

df_sesiones['timestamp'] = pd.to_datetime(df_sesiones['timestamp'])

df_sesiones['timestamp'] = df_sesiones['timestamp'].dt.tz_convert('Etc/GMT+5')

# Eliminar los microsegundos, segundos y la zona horaria
df_sesiones['timestamp'] = df_sesiones['timestamp'].dt.floor('min')

df_sesiones = df_sesiones[['id', 'id_usuario', 'tipo_cierre', 'timestamp']]

sesiones_csv_salida = '../resultados/fact_sesiones.csv'
df_sesiones.to_csv(sesiones_csv_salida, index=False)

print(f"Datos transformados y guardados en '{sesiones_csv_salida}'")