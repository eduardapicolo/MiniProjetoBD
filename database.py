from pymongo import MongoClient

uri = "mongodb+srv://adm:adm777@mensageria.dmgoipc.mongodb.net/"
client = MongoClient(uri)

def userAuthentication(user, password):
    try:
        database = client.get_database("Mensageria")
        users = database.get_collection("Users")

        query = { "email": user, "senha": password }
        account = users.find_one(query)

        if account:
            print(f"Bem-vindo, {account['nomeDeUsuario']}")
            return True
        else:
            print(f"Senha incorreta.")
            return False

    except Exception as e:
        raise Exception("Não foi possível encontrar o documento devido ao seguinte erro: ", e)
