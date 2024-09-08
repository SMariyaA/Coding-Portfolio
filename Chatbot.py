def chatbot_response(user_input):
    responses = {
        'hello': 'Hi there!',
        'how are you': 'I am good, thank you!',
        'bye': 'Goodbye!',
        'nice to meet you': 'likewise'
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
