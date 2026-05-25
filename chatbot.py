

print(" Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:

    user_input = input("You: ").lower()

    
    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine and ready to assist you!")

    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input == "who made you":
        print("Bot: I was created by a Python developer.")

    elif user_input == "help":
        print("Bot: You can ask simple questions like:")
        print("- hello")
        print("- how are you")
        print("- what is your name")

    # Exit command
    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand that.")