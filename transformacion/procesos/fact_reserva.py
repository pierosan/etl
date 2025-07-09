import pandas as pd
from io import StringIO

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
df_usuarios.rename(columns={'id': 'id_usuario'}, inplace=True)

# se ordena la tabla dispositivos y se selecciona lo principal
df_dispositivos = df_dispositivos[['id', 'id_origen']] 
# se renombra la columna 
df_dispositivos.rename(columns={'id': 'id_dispositivo'}, inplace=True)

# crea una nueva columna 'id' de 1 a N
df_reservas['id'] = range(1, len(df_inactividad) + 1) 
# renombra la columna 'usuario_id' a 'id_origen_usuario'
df_inactividad.rename(columns={'usuario_id': 'id_origen_usuario'}, inplace=True)

# une 'df_inactividad' con 'df_usuarios' en 'df_inactividad'
df_inactividad = pd.merge(
    df_inactividad,
    df_usuarios,
    left_on='id_origen_usuario', # Columna id_usuario del CSV de inactividad
    right_on='id_origen', # Columna de usuarios que contiene el ID de origen
    how='left' # Usamos left join para mantener todas las filas de fact_inactividad
)

# 4. Convertir 'hora_inactividad' a formato datetime
df_inactividad['hora_inactividad'] = pd.to_datetime(df_inactividad['hora_inactividad'])

# Seleccionar solo las columnas deseadas para fact_inactividad
df_inactividad = df_inactividad[['id', 'id_usuario', 'hora_inactividad']]

# --- Guardar el resultado ---
inactividad_csv_salida = '../resultados/fact_inactividad.csv'
df_inactividad.to_csv(inactividad_csv_salida, index=False)

print(f"Datos transformados y guardados en '{inactividad_csv_salida}'")
