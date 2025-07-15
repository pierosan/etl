from Crypto.Cipher import AES
import os

def descifrar_texto(texto_cifrado):
    print("desencriptando credenciales...")
    LLAVE = os.getenv('LLAVE')
    LLAVE = bytes.fromhex(LLAVE)

    iv = b'8ZNh7tU$cTWd2*Rd'

    texto_cifrado_byte = bytes.fromhex(texto_cifrado)

    cifrador = AES.new(LLAVE, AES.MODE_CFB, iv)
    byte_texto = cifrador.decrypt(texto_cifrado_byte)
    texto = byte_texto.decode('utf-8')
    print("credenciales desencriptadas\n")
    return texto
    #print(f"Texto:\n{texto}")