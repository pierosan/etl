import os
import dotenv
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# Carga de variables de entorno
dotenv.load_dotenv()

print("Iniciando proceso ETL\n")

# proceso de extraccion
from procesos.extraer import extraer
print("Iniciando proceso de extraccion\n")
df_usuario, df_dispositivo, df_inactividad, df_reserva, df_sesion, df_ubicacion = extraer.iniciar()


# proceso de transformacion
print("\nIniciando proceso de transformacion\n")
from procesos.transformar import transformar
df_usuario, df_dispositivo, df_inactividad, df_reserva, df_sesion, df_ubicacion = transformar.iniciar(df_usuario, df_dispositivo, df_inactividad, df_reserva, df_sesion, df_ubicacion)


# proceso de carga
print("\nIniciando proceso de carga\n")
from procesos.carga import carga
carga.borrar_tablas()
carga.crear_tablas()
carga.iniciar(df_usuario, df_dispositivo, df_inactividad, df_reserva, df_sesion, df_ubicacion)
