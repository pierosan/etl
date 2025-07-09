import pandas as pd
from io import StringIO

# --- Carga de datos ---
dispositivos_csv = '../../extraccion/colecciones/dispositivos.csv'
df = pd.read_csv(dispositivos_csv)

# --- Transformación de datos ---
# remplaza id por id_origen para mantener las referencias del id original 
df = df.rename(columns={'id': 'id_origen'})

# renombrar 'fechaCreacion' a 'fecha_creacion'
df = df.rename(columns={'nfcId': 'id_nfc'})

# renombrar 'id_dispositivo' a 'num_dispositivo'
df = df.rename(columns={'id_dispositivo': 'num_dispositivo'})

# generar id secuenciales de 1 a n
df.insert(0, 'id', range(1, 1 + len(df)))

# reordenar las columnas 
df = df[['id', 'num_dispositivo', 'descripcion', 'ubicacion', 'id_nfc', 'estado', 'usuario_asignado', 'fecha_registro', 'id_origen']]

# transforma dni de texto a entero
df['num_dispositivo'] = df['num_dispositivo'].astype(int)

# transforma la fecha a formato datetime
df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])

# --- Guardar el resultado ---
dispositivos_csv_salida = '../resultados/dim_dispositivo.csv'
df.to_csv(dispositivos_csv_salida, index=False)

print(f"Datos transformados y guardados en '{dispositivos_csv_salida}'")