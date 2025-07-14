from Crypto.Cipher import AES
import dotenv
import os
dotenv.load_dotenv()

LLAVE = os.getenv('LLAVE')
LLAVE = bytes.fromhex(LLAVE)

iv = b'8ZNh7tU$cTWd2*Rd'

texto = "a"
byte_texto = texto.encode('utf-8')

cifrador = AES.new(LLAVE, AES.MODE_CFB, iv)
texto_cifrado_byte = cifrador.encrypt(byte_texto)

texto_cifrado = texto_cifrado_byte.hex()

print(f"Texto cifrado:\n{texto_cifrado}")