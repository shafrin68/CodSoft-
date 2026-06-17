# Rule-Based Chatbot

print("Welcome to the Simple Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user_input:
        print("Bot: My name is RuleBot.")

    elif "help" in user_input:
        print("Bot: I can answer simple questions like greetings, time, and date.")

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
