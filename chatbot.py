def chatbot():
    print(" Hello! I am your AI chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hello! How are you? ")

        elif "your name" in user_input:
            print("Bot: My name is MiniBot. ")

        elif "how are you" in user_input:
            print("Bot: I am doing great! How can I help you?")

        elif "what can you do" in user_input:
            print("Bot: I can chat with you and answer basic questions.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day! ")
            break

        else:
            print("Bot: Sorry, I don't understand that yet.")


chatbot()
