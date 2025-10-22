import database

def sendMessages(user):
    print("\n=== ENVIAR MENSAGEM ===")

    to = input("Para (nome de usuário do destinatário): ").strip()
    title = input("Título da mensagem: ").strip()
    text = input("Conteúdo da mensagem: ").strip()
    password_key = input("Chave secreta compartilhada (para criptografia): ").strip()

    if not to or not title or not text or not password_key:
        print("\nTodos os campos são obrigatórios.")
        input("Pressione Enter para voltar ao menu...")
        return

    if not database.userExists(to):
        print(f"\nO usuário '{to}' não existe.")
        input("Pressione Enter para voltar ao menu...")
        return

    try:
        success = database.sendMessage(user, to, title, text, password_key)

        if success:
            print("\nMensagem enviada com sucesso!")
            print("Lembre-se de compartilhar a CHAVE SECRETA com o destinatário.")
            print("Ele precisará dela para descriptografar a mensagem.")
        else:
            print("\nFalha ao enviar a mensagem. Verifique os dados e tente novamente.")

    except Exception as e:
        print(f"\nOcorreu um erro ao enviar a mensagem: {e}")

    input("\nPressione Enter para voltar ao menu...")
