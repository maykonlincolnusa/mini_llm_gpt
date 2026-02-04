def chat_loop():
    print("Chat iniciado")
    while True:
        msg = input("> ")
        if msg == "exit":
            break
        print("Bot:", msg[::-1])  # placeholder
