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

def encrypt_password(password, key):
    if not key:
        print("Chave inválida. Não é possível criptografar a mensagem.")
        return None
    
    try:
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password.encode('utf-8'))
        return encrypted_password
    except Exception as e:
        print(f"Erro ao criptografar a senha: {e}")
        return None
    
def decrypt_password(encrypted_password, key):
    if not key:
        print("Chave inválida. Não é possível descriptografar a mensagem.")
        return None
    
    try:
        fernet = Fernet(key)
        decrypted_password = fernet.decrypt(encrypted_password)
        return decrypted_password.decode('utf-8')
    except Exception as e:
        print(f"Erro ao descriptografar a senha: {e}")
        return None

# Permite que você gere a chave executando: python crypto.py
if __name__ == "__main__":
    print("Gerando nova chave de criptografia...")
    generate_key()
