def chatbot(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "My name is SimpleBot."

    elif user_input == "who are you":
        return "I am a simple rule-based chatbot."

    elif user_input == "what can you do":
        return "I can respond to simple questions and greetings."

    elif user_input == "good morning":
        return "Good morning! Have a great day!"

    elif user_input == "good afternoon":
        return "Good afternoon! How can I help you?"

    elif user_input == "good evening":
        return "Good evening! What can I do for you?"

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    elif user_input == "what is python":
        return "Python is a popular programming language."

    elif user_input == "what is coding":
        return "Coding is the process of writing instructions for a computer."

    elif user_input == "help":
        return "You can say hello, ask how I am, ask my name, or say bye."

    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."


print("SIMPLE RULE-BASED BOT")
print("Type 'help' to see what I can do.")
print("Type 'bye' to exit the chatbot.")
print()

while True:
    user_input = input("You: ")

    if user_input.strip() == "":
        print("Bot: Please enter something.")
        continue

    response = chatbot(user_input)

    print("Bot:", response)

    if user_input.lower().strip() == "bye" or user_input.lower().strip() == "goodbye":
        break

print("Chatbot ended.")