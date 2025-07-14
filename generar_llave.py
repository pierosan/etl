import secrets
llave = secrets.token_bytes(32)
print(f"Llave:\n{llave.hex()}")