from pymongo import MongoClient
from connectionString import connectionString
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
        return False

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
            return False

    except Exception as e:
        raise Exception("Não foi possível encontrar o documento devido ao seguinte erro: ", e)


#TODO ADICIONAR DESCRIPTOGRAFIA
def getMessages(User):
    if User == None:
        return None
    
    try:
        database = client.get_database("Mensageria")
        messages = database.get_collection("Messages")

        query = { "to": User.username }
        messagesFound = messages.find(query)

        if messagesFound:
            listOfMessages = []
            for m in messagesFound:
                if m['status'] == False:
                    messageAux = Message(m['_id'],
                                         m['from'],
                                         m['to'],
                                         m['titulo'],
                                         m['mensagem'],
                                         "Nao lida.")
                    
                    listOfMessages.append(messageAux)
                
                elif m['status'] == True:
                    messageAux = Message(m['_id'],
                                         m['from'],
                                         m['to'],
                                         m['titulo'],
                                         m['mensagem'],
                                         "Lida.")
                    listOfMessages.append(messageAux)
            
            return listOfMessages

        return None

    except Exception as e:
        raise Exception("Não foi possível encontrar o documento devido ao seguinte erro: ", e)

#TODO ADICIONAR CRIPTOGRAFIA
def sendMessage(User, to, title, text):
    if User == None or to == None or title == None or text == None:
        return False
    
    try:
        database = client.get_database("Mensageria")
        messages = database.get_collection("Messages")

        message = {
            "from": User.username,
            "to": to,
            "titulo": title,
            "mensagem": text,
            "status": False
        }

        messages.insert_one(message)
        return True

    except Exception as e:
        raise Exception("Não foi possível inserir o documento devido ao seguinte erro: ", e)
