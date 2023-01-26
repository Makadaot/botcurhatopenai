while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "help":
        print("Chatbot: Available commands are 'help' and 'exit'")
    else:
        bot_response = chatbot_response(user_input)
        print("Chatbot: " + bot_response)
