import firebase_admin
from firebase_admin import credentials, firestore

LLAVE_PRIVADA =  'key.json'

def conexion():
    try:
        print("Iniciando conexion a Firebase Admin SDK")
        credenciales = credentials.Certificate(LLAVE_PRIVADA)
        firebase_admin.initialize_app(credenciales)
        db = firestore.client()
        print("Firebase Admin SDK conectado")
        return db
    except Exception as e:
        print(f"Error al conectarse a Firebase Admin SDK: {e}")
        exit()
