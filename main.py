import database
import viewMessages
import sendMessages

def main():
    print("\n=== BEM-VINDO(A) AO SISTEMA DE MENSAGERIA ===")

    currentUser = None

    # -------- MENU DE LOGIN / CADASTRO --------
    while currentUser is None:
        print("\n1. Fazer login")
        print("2. Cadastrar novo usuário")
        print("3. Sair")

        option = input("Escolha uma opção: ")

        if option == '1':
            # ---- LOGIN ----
            email = input("Email: ").strip()
            password = input("Senha: ").strip()

            currentUser = database.userAuthentication(email, password)

            if not currentUser:
                print("\n Login falhou. Email ou senha incorretos.\n")
                currentUser = None
            else:
                print(f"\n Login bem-sucedido! Bem-vindo(a), {currentUser.username}.")

        elif option == '2':
            # ---- CADASTRO ----
            print("\n=== CADASTRO DE NOVO USUÁRIO ===")
            email = input("Digite seu email: ").strip()
            password = input("Crie uma senha: ").strip()
            username = input("Crie um nome de usuário (sem espaços): ").strip()

            success = database.registerUser(email, password, username)
            if success:
                print("\n Usuário cadastrado com sucesso!")
                print("Agora você pode fazer login com suas credenciais.")
            else:
                print("\n Falha ao cadastrar. Tente novamente.")

            input("\nPressione Enter para continuar...")

        elif option == '3':
            print("\nSaindo do sistema...")
            return

        else:
            print("\n Opção inválida. Tente novamente.\n")

    # -------- MENU PRINCIPAL (após login) --------
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Visualizar mensagens novas")
        print("2. Enviar mensagem")
        print("3. Logout / Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            viewMessages.viewNewMessages(currentUser)

        elif choice == '2':
            sendMessages.sendMessages(currentUser)
        elif choice == '3':
            print("\n Encerrando sessão...")
            currentUser = None
            print("Você foi deslogado com sucesso.")
            break

        else:
            print("\nOpção inválida. Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()            