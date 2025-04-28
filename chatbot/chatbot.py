import requests

TOGETHER_API_KEY = "4764db21a81b22c5bf17774ce2aa638ba872bd157688403deee710f18a8bebc0"

headers = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"   # Updated correct model name

def chat_with_bot(message):
    url = "https://api.together.ai/v1/chat/completions"
    
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": message}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        bot_reply = result["choices"][0]["message"]["content"]
        return bot_reply
    else:
        return f"Error {response.status_code}: {response.text}"

# Example conversation loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    bot_response = chat_with_bot(user_input)
    print(f"Bot: {bot_response}")
