import pandas as pd

# --- Carga de datos ---
usuarios_csv = '../resultados/dim_usuario.csv'
df_usuarios = pd.read_csv(usuarios_csv)

dispositivos_csv = '../../extraccion/colecciones/dispositivos.csv'
df_dispositivos = pd.read_csv(dispositivos_csv)

# --- Transformación de datos ---
# se ordena la tabla usuarios y se selecciona lo principal
df_usuarios = df_usuarios[['id', 'nombre']] 
# se renombra la columna 
df_usuarios.rename(columns={'id': 'id_usuario', 'nombre': 'nombre_usuario'}, inplace=True)

# remplaza id por id_origen para mantener las referencias del id original 
df_dispositivos = df_dispositivos.rename(columns={'id': 'id_origen', 'nfcId': 'id_nfc', 'id_dispositivo': 'num_dispositivo'})

# generar id secuenciales de 1 a n
df_dispositivos.insert(0, 'id', range(1, 1 + len(df_dispositivos)))

df_dispositivos = pd.merge(
    df_dispositivos,
    df_usuarios,
    left_on='usuario_asignado', # Columna id_usuario del CSV de inactividad
    right_on='nombre_usuario', # Columna de usuarios que contiene el ID de origen
    how='left' # Usamos left join para mantener todas las filas de fact_inactividad
)

# reordenar las columnas 
df_dispositivos = df_dispositivos[['id', 'num_dispositivo', 'descripcion', 'ubicacion', 'id_nfc', 'estado', 'id_usuario', 'fecha_registro', 'id_origen']]

# transforma dni de texto a entero
df_dispositivos['num_dispositivo'] = df_dispositivos['num_dispositivo'].astype(int)

# transforma la fecha a formato datetime
df_dispositivos['fecha_registro'] = pd.to_datetime(df_dispositivos['fecha_registro'])

df_dispositivos['fecha_registro'] = df_dispositivos['fecha_registro'].dt.tz_convert('Etc/GMT+5')

# Eliminar los microsegundos, segundos y la zona horaria
df_dispositivos['fecha_registro'] = df_dispositivos['fecha_registro'].dt.floor('min')

# --- Guardar el resultado ---
dispositivos_csv_salida = '../resultados/dim_dispositivo.csv'
df_dispositivos.to_csv(dispositivos_csv_salida, index=False)

print(f"Datos transformados y guardados en '{dispositivos_csv_salida}'")