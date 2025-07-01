
---

## simple-ai-chatbot/simple_chatbot.py

```python
import openai

openai.api_key = "YOUR_API_KEY"

def chatbot():
    print("Chatbot is running. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=150,
        )
        print("Bot:", response['choices'][0]['message']['content'])

if __name__ == "__main__":
    chatbot()
