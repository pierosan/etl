import pandas as pd

# --- Carga de datos ---
dispositivos_csv = '../resultados/dim_dispositivo.csv'
df_dispositivos = pd.read_csv(dispositivos_csv)

ubicacion_gps_csv = '../../extraccion/colecciones/registro_ubicacion_dispositivos.csv'
df_ubicacion_gps = pd.read_csv(ubicacion_gps_csv)

# se ordena la tabla dispositivos y se selecciona lo principal
df_dispositivos = df_dispositivos[['id', 'descripcion']] 
# se renombra la columna 
df_dispositivos.rename(columns={'id': 'id_dispositivo', 'descripcion': 'nombre_descripcion'}, inplace=True)

# crea una nueva columna 'id' de 1 a N
df_ubicacion_gps['id'] = range(1, len(df_ubicacion_gps) + 1) 
# se renombra
df_ubicacion_gps.rename(columns={'dispositivo': 'nombre_descripcion_fk'}, inplace=True)
# se ordena
df_ubicacion_gps = df_ubicacion_gps[['id', 'nombre_descripcion_fk', 'timestamp', 'latitud', 'longitud']]

df_ubicacion_gps = pd.merge(
    df_ubicacion_gps,
    df_dispositivos,
    left_on='nombre_descripcion_fk', # Columna id_usuario del CSV de inactividad
    right_on='nombre_descripcion', # Columna de usuarios que contiene el ID de origen
    how='left' # Usamos left join para mantener todas las filas de fact_inactividad
)

df_ubicacion_gps = df_ubicacion_gps.dropna(subset=['id_dispositivo'])

# 4. Convertir 'hora_inactividad' a formato datetime
df_ubicacion_gps['timestamp'] = pd.to_datetime(df_ubicacion_gps['timestamp'])

# Seleccionar solo las columnas deseadas para fact_inactividad
df_ubicacion_gps = df_ubicacion_gps[['id', 'id_dispositivo', 'timestamp', 'latitud', 'longitud']]

# --- Guardar el resultado ---
ubicacion_gps_csv_salida = '../resultados/fact_ubicacion_gps.csv'
df_ubicacion_gps.to_csv(ubicacion_gps_csv_salida, index=False)


print(f"Datos transformados y guardados en '{ubicacion_gps_csv_salida}'")