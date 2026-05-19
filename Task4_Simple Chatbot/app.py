def chatbot():
    print("🤖 Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Remove punctuation
        user_input = user_input.replace("!", "").replace("?", "").replace(".", "")

        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hi!")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm fine, thanks!")

        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye!")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")


chatbot()
