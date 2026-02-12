import ollama

history = []

while True:
    print("Ask something from DavutAI (press q or e to exit)")
    prompt = input("You:  ")

    if (prompt in ["q", "e"]):
        print("Have a nice day")
        break

    message = {
        "role": "user",
        "content": prompt
    }

    history.append(message)

    print( "Bot:  ", end="", flush=True )

    response = ollama.chat(
        model = "llama2",
        messages = history,
        stream = True
    )

    bot_msg_response = ""

    for chunk in response:
        bot_msg_response += chunk["message"]["content"]
        print(chunk["message"]["content"] , end="", flush=True)
    
    bot_message = {
        "role": "assistant",
        "content": bot_msg_response
    }

    history.append(bot_message)
    