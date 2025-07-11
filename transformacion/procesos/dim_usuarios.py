import pandas as pd
from io import StringIO

# --- Carga de datos ---
usuarios_csv = '../../extraccion/colecciones/usuarios.csv'
df = pd.read_csv(usuarios_csv)

# --- Transformación de datos ---
# remplaza id por id_origen para mantener las referencias del id original 
df = df.rename(columns={'id': 'id_origen'})

# renombrar 'fechaCreacion' a 'fecha_creacion'
df = df.rename(columns={'fechaCreacion': 'fecha_creacion'})

# generar id secuenciales de 1 a n
df.insert(0, 'id', range(1, 1 + len(df)))

# reordenar las columnas 
df = df[['id', 'nombre', 'dni', 'area', 'empresa', 'fecha_creacion', 'id_origen']]

# transforma dni de texto a entero
df['dni'] = df['dni'].astype(int)

# transforma la fecha a formato datetime
df['fecha_creacion'] = pd.to_datetime(df['fecha_creacion'])

df['fecha_creacion'] = df['fecha_creacion'].dt.tz_convert('Etc/GMT+5')

# Eliminar los microsegundos, segundos y la zona horaria
df['fecha_creacion'] = df['fecha_creacion'].dt.floor('min')

# --- Guardar el resultado ---
usuarios_csv_salida = '../resultados/dim_usuario.csv'
df.to_csv(usuarios_csv_salida, index=False)

print(f"Datos transformados y guardados en '{usuarios_csv_salida}'")