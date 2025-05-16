import cohere

API_KEY = ""
co = cohere.Client(api_key=API_KEY)
if not API_KEY:
    print("No API Key entered. Please enter a valid key to use the script.")

def ask_llm(question):
    """Send a message to Cohere's Command R+ model and return the response."""
    try:
        response = co.chat(
            model="command-r-plus",
            message=question,
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def chat_loop():
    """Simple loop for chatting with Cohere."""
    print("Chat with Cohere (type 'exit' to quit):")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        reply = ask_llm(user_input)
        print(f"Cohere: {reply}\n")

if __name__ == "__main__":
    chat_loop()
