from pymongo import MongoClient
from connectionString import connectionString

uri = connectionString
client = MongoClient(uri)

def userAuthentication(user, password):
    try:
        database = client.get_database("Mensageria")
        users = database.get_collection("Users")

        query = { "email": user, "senha": password }
        account = users.find_one(query)

        if account:
            #Mensagem de "boas vindas"
            return True
        else:
            #Mensagem de erro ("Email ou senha incorreto.")
            return False

    except Exception as e:
        raise Exception("Não foi possível encontrar o documento devido ao seguinte erro: ", e)
