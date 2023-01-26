stage = 0
topic = ""
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    elif stage == 0:
        if "hello" in user_input.lower():
            stage = 1
            bot_response = "Hello! How can I help you today?"
        else:
            bot_response = "I'm sorry, I didn't understand what you said. Could you please rephrase it?"
    elif stage == 1:
        if "help" in user_input.lower():
            topic = "help"
            stage = 2
            bot_response = "What kind of help do you need?"
        elif "weather" in user_input.lower():
            topic = "weather"
            stage = 2
            bot_response = "What location do you want the weather for?"
        else:
            bot_response = "I'm sorry, I didn't understand what you said. Could you please rephrase it?"
    elif stage == 2:
        if topic == "help":
            bot_response
