from openai import OpenAI

# 1. Initialize the new client object with your API key
client = OpenAI(
    api_key="put your own key:")

def chat_with_gpt(prompt):
    # 2. Use the new chat completions syntax format
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]  # Changed 'message' to 'messages'
    )
    # 3. Access properties using dot notation instead of a dictionary
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        
        # Fixed .lower() to include parentheses so it executes the function
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
            
        response = chat_with_gpt(user_input)
        print("chatbot:", response)
