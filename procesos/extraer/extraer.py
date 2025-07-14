from db import db_firebase
import pandas as pd

db = db_firebase.conexion()

def extraccion(ref_coleccion, nombre_coleccion):
    print(f"Exportando colección: {nombre_coleccion}...")
    docs = ref_coleccion.stream()
    data = []
    total = len(list(ref_coleccion.stream()))

    for index,doc in enumerate(docs):
        doc_data = doc.to_dict()
        doc_data['id'] = doc.id  
        data.append(doc_data)
        print(f"[{index+1}/{total}] Extrayendo...")

    if data:
        df = pd.DataFrame(data)
        return df
    else:
        print(f"La colección '{nombre_coleccion}' está vacía. No se creó a extraido nada")

def get_colecciones(db):
    colecciones = db.collections()
    nombre_coleccion = [col.id for col in colecciones]
    return nombre_coleccion

def iniciar():
    # Obtener todas las colecciones de nivel superior
    colecciones = get_colecciones(db)

    if not colecciones:
        print("No se encontraron colecciones de nivel superior en la base de datos.")
    else:
        print(f"Colecciones encontradas: {colecciones}")
        coleccion_usuario = db.collection('usuarios')
        coleccion_dispositivo = db.collection('dispositivos')
        coleccion_inactividad = db.collection('registro_inactividad')
        coleccion_reservas = db.collection('reservas')
        coleccion_sesiones = db.collection('registro_sesiones')
        coleccion_ubicacion = db.collection('registro_ubicacion_dispositivos')

        df_usuario = extraccion(coleccion_usuario, 'usuarios')
        df_dispositivo = extraccion(coleccion_dispositivo, 'dispositivos')
        df_inactividad = extraccion(coleccion_inactividad, 'registro_inactividad')
        df_reserva = extraccion(coleccion_reservas, 'reservas')
        df_sesion = extraccion(coleccion_sesiones, 'registro_sesiones')
        df_ubicacion = extraccion(coleccion_ubicacion, 'registro_ubicacion_dispositivos')
        
        print("\nProceso de extraccion completado.")

        return df_usuario, df_dispositivo, df_inactividad, df_reserva, df_sesion, df_ubicacion