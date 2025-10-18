#VERSÃO ONDE A CHAVE É CONVERSADA VERBALMENTE
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


STATIC_SALT = b'minha_app_de_mensagens_secreta_salt_123'

#Transforma a senha na chave de criptografia valida para o FERNET
def derive_key(password: str) -> bytes:

    password_bytes = password.encode()
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32, 
        salt=STATIC_SALT,
        iterations=100000, 
        backend=default_backend()
    )
    
    key_bytes = kdf.derive(password_bytes)
    
    fernet_key = base64.urlsafe_b64encode(key_bytes)
    return fernet_key


"""
VERSAO ONDE A CHAVE E GERADA AUTOMATICAMENTE 
#é preciso rodar esse arquivo UMA VEZ para criar o arquivo
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def generate_key():

    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f"Chave gerada e salva em '{KEY_FILE}'")
    print("Guarde esta chave em segurança! Ela é necessária para ler e enviar mensagens.")

def load_key():

    try:
        return open(KEY_FILE, "rb").read()
    except FileNotFoundError:
        print(f"Erro: Arquivo de chave '{KEY_FILE}' não encontrado.")
        print("Você precisa gerar a chave primeiro.")
        print(f"Execute: python {__file__}")
        return None

# Permite que você gere a chave executando: python crypto.py
if __name__ == "__main__":
    print("Gerando nova chave de criptografia...")
    generate_key()
"""