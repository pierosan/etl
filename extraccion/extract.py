import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import os

# --- Configuración ---
# Ruta a tu archivo de clave privada (asegúrate de que sea la ruta correcta)
LLAVE_PRIVADA = 'key.json'
# Directorio donde se guardarán los archivos CSV
CARPETA_SALIDA = 'colecciones'

# --- Inicializar Firebase Admin SDK ---
try:
    credenciales = credentials.Certificate(LLAVE_PRIVADA)
    firebase_admin.initialize_app(credenciales)
    db = firestore.client()
    print("Firebase Admin SDK conectado")
except Exception as e:
    print(f"Error al conectarse a Firebase Admin SDK: {e}")
    exit()

# Crear el directorio de salida si no existe
if not os.path.exists(CARPETA_SALIDA):
    print(f"Directorio '{CARPETA_SALIDA}' no existe, creandose...")
    os.makedirs(CARPETA_SALIDA)
    print(f"Directorio '{CARPETA_SALIDA}' creado.")


# --- Funciones ---
def exportar(ref_coleccion, nombre_coleccion):
    # Exporta una colección de Firestore a un archivo CSV.
    print(f"Exportando colección: {nombre_coleccion}...")
    docs = ref_coleccion.stream()
    data = []
    
    for doc in docs:
        doc_data = doc.to_dict()
        doc_data['id'] = doc.id  # Añadir el ID del documento
        data.append(doc_data)

    if data:
        # Usar pandas para crear un DataFrame y guardarlo como CSV
        df = pd.DataFrame(data)
        nombre_csv = os.path.join(CARPETA_SALIDA, f'{nombre_coleccion}.csv')
        df.to_csv(nombre_csv, index=False)
        print(f"Colección '{nombre_coleccion}' exportada a '{nombre_csv}'")
    else:
        print(f"La colección '{nombre_coleccion}' está vacía. No se creó ningún archivo CSV.")

def get_colecciones(db):
    # Obtiene todas las colecciones de nivel superior en la base de datos Firestore.
    colecciones = db.collections()
    nombre_coleccion = [col.id for col in colecciones]
    return nombre_coleccion

# Obtener todas las colecciones de nivel superior
colecciones = get_colecciones(db)

if not colecciones:
    print("No se encontraron colecciones de nivel superior en la base de datos.")
else:
    print(f"Colecciones encontradas: {colecciones}")
    for nombre_coleccion in colecciones:
        ref_coleccion = db.collection(nombre_coleccion)
        exportar(ref_coleccion, nombre_coleccion)

print("\nProceso de exportación completado.")