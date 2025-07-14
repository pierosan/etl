from Crypto.Cipher import AES
import dotenv
import os
dotenv.load_dotenv()

LLAVE = os.getenv('LLAVE')
LLAVE = bytes.fromhex(LLAVE)

iv = b'8ZNh7tU$cTWd2*Rd'

texto_cifrado = "e8"
texto_cifrado_byte = bytes.fromhex(texto_cifrado)

cifrador = AES.new(LLAVE, AES.MODE_CFB, iv)
byte_texto = cifrador.decrypt(texto_cifrado_byte)
texto = byte_texto.decode('utf-8')

print(f"Texto:\n{texto}")