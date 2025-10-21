import database

def viewNewMessages(user):

    print("Buscando mensagens não lidas...")
    unread_messages = database.getUnreadMessages(user)

    if not unread_messages:
        print("\nVocê não tem mensagens novas.")
        input("Pressione Enter para voltar ao menu...")
        return

    print(f"\nVocê tem {len(unread_messages)} mensagens novas:")
    
    for msg in unread_messages:
        print(f"  ID: {msg.mId}")
        print(f"  De: {msg.sentBy}")
        print(f"  Título: {msg.title}")
        print("  --------------------")
    
    msg_id_input = input("\nDigite o ID da mensagem que você quer ler (ou 's' para sair): ")

    if msg_id_input.lower() == 's':
        return
    
    selected_message = None
    for msg in unread_messages:
        if str(msg.mId) == msg_id_input:
            selected_message = msg
            break
    
    if not selected_message:
        print("ID inválido. Tente novamente.")
        input("Pressione Enter para voltar...")
        viewNewMessages(user) 
        return

    print(f"--- Lendo Mensagem de: {selected_message.sentBy} ---")
    print(f"Título: {selected_message.title}\n")
    
    password_key_input = input("DIGITE A CHAVE SECRETA (combinada com o remetente): ")

    decrypted_content = database.decryptMessage(selected_message.text, password_key_input)

    if decrypted_content == False:
        print("\n--- !! CHAVE INCORRETA !! ---")
        print("Acesso à mensagem negado.")
    else:
        print("\n--- CHAVE CORRETA ---")
        print("Mensagem descriptografada:\n")
        print(decrypted_content)
        
        database.markMessageAsRead(selected_message.mId)
        print("\n(Mensagem marcada como lida)")

    input("\nPressione Enter para voltar ao menu...")
