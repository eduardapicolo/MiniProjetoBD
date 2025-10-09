class Message:
    def __init__(self, mId, sentBy, to, title, text, status):
        self.mId = mId
        self.sentBy = sentBy
        self.to = to
        self.title = title
        self.text = text
        self.status = status

    def __str__(self):
        return("---------------------\n"
               f"Id: {self.mId}\n"
               f"De: {self.sentBy}\n"
               f"Para: {self.to}\n"
               f"Mensagem: {self.text}\n"
               f"Status: {self.status}\n"
               "---------------------\n")