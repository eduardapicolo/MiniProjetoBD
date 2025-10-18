import database
import viewMessages

def main():
    print ("--- BEM-VINDO(A) AO SISTEMA DE MENSAGERIA ---")
    #TODO LOGIN
    #esse codigo é apenas para testar o viewmessages. É preciso realmente verificar

    currentUser = None
    while currentUser is None:
        email = input("Email: ")
        password = input("Senha: ")
        
        currentUser = database.userAuthentication(email, password)

        if not currentUser:
            print("Login falhou. Email ou senha incorretos. Tente novamente.\n")
        else:
            print(f"Login bem-sucedido! Bem-vindo, {currentUser.username}.")

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Visualizar mensagens novas")
        print("2. Enviar mensagem")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            viewMessages.viewNewMessages(currentUser)
        elif choice == '2':
            print("fazer..")
            #TODO enviar msg
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()            