from . import dim_usuario_transformar, dim_dispositivo_transformar, fact_inactividad_transformar, fact_reserva_transformar, fact_sesion_transformar, fact_ubicacion_gps_transformar

def iniciar(df_usuario, df_dispositivo, df_inactividad, df_reserva, df_sesion, df_ubicacion):

    df_usuario = dim_usuario_transformar.tranformacion(df_usuario)
    df_dispositivo = dim_dispositivo_transformar.tranformacion(df_dispositivo, df_usuario)
    df_inactividad = fact_inactividad_transformar.tranformacion(df_inactividad, df_usuario)
    df_reserva = fact_reserva_transformar.tranformacion(df_reserva, df_usuario, df_dispositivo)
    df_sesion = fact_sesion_transformar.tranformacion(df_sesion, df_usuario)
    df_ubicacion = fact_ubicacion_gps_transformar.tranformacion(df_ubicacion, df_dispositivo)

    print("\nProceso de transformacion completado.")
    
    return df_usuario, df_dispositivo, df_inactividad, df_reserva, df_sesion, df_ubicacion

