from pymongo import MongoClient
from connectionString import connectionString
from crypto import derive_key
from cryptography.fernet import Fernet, InvalidToken
from user import User
from message import Message

uri = connectionString
client = MongoClient(uri)

#Olá pessoa que está criando a parte de login, irei explicar como funciona esse código de autenticação.
#Ao chamar a função, será passado o email e senha do usuário.
#Após toda a verificação será retornado a classe do usuário, se o login for efetuado.
#Caso contrário, retornará false.
def userAuthentication(email, password):
    if email == None or password == None:
        return None

    try:
        database = client.get_database("Mensageria")
        users = database.get_collection("Users")

        query = { 
                  "email": email, 
                  "senha": password 
                }
        account = users.find_one(query)

        if account:
            currentUser = User(account['_id'],
                               account['email'],
                               account['senha'],
                               account['nomeDeUsuario'])
            return currentUser
        
        else:
            return None

    except Exception as e:
        raise Exception("Não foi possível encontrar o documento devido ao seguinte erro: ", e)



#Busca as mensagens onde o Status é FALSE apenas
def getUnreadMessages(User):
    if User == None:
        return None
    
    try:
        database = client.get_database("Mensageria")
        messages = database.get_collection("Messages")

        query = { "to": User.username,
                 "status": False }
        messagesFound = messages.find(query)

        if messagesFound:
            listOfMessages = []
            for m in messagesFound:
                    messageAux = Message(m['_id'],
                                         m['from'],
                                         m['to'],
                                         m['titulo'],
                                         m['mensagem'],
                                         "Nao lida.")
                    
                    listOfMessages.append(messageAux)
            
            return listOfMessages

        return None

    except Exception as e:
        raise Exception("Não foi possível encontrar o documento devido ao seguinte erro: ", e)

#Com criptografia
def sendMessage(user, to, title, text, password_key):
    if user == None or to == None or title == None or text == None:
        return False
    
    try:
        fernet_key = derive_key(password_key)
        fernet = Fernet(fernet_key)
        
        encrypted_text = fernet.encrypt(text.encode())

        database = client.get_database("Mensageria")
        messages = database.get_collection("Messages")

        message = {
            "_id": messages.estimated_document_count() + 1,
            "from": user.username,
            "to": to,
            "titulo": title,
            "mensagem": encrypted_text,
            "status": False
        }

        messages.insert_one(message)
        return True

    except Exception as e:
        raise Exception("Não foi possível inserir o documento devido ao seguinte erro: ", e)

#função para descriptografar
def decryptMessage(encrypted_text, password_key: str):

    try:
        fernet_key = derive_key(password_key)
        fernet = Fernet(fernet_key)
        
        decrypted_text = fernet.decrypt(encrypted_text).decode()
        return decrypted_text
    except InvalidToken:
        return False
    except Exception as e:
        print(f"Erro ao descriptografar: {e}")
        return False
    
#função para mudar o STATUS após a msg ser lida        
def markMessageAsRead(message_id):

    try:
        database = client.get_database("Mensageria")
        messages = database.get_collection("Messages")
        
        query = { "_id": message_id }
        update = { "$set": { "status": True } }
        
        result = messages.update_one(query, update)
        return result.modified_count > 0
        
    except Exception as e:
        print(f"Erro ao atualizar status da mensagem: {e}")
        return False    
