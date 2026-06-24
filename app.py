from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


print("AI Chatbot Started")
print("Type exit to quit")
conversation=[]

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    if user_input.lower() == "clear":
        conversation = []
        print("Memory cleared!")
        continue

    conversation.append({
        "role": "user",
        "content": user_input
    })

    history = ""

    for msg in conversation:
        history +=f"{msg['role']}: {msg['content']}\n"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history
    )

    ai_reply = response.text

    print("\nAI:", ai_reply)

    conversation.append({
        "role": "assistant",
        "content": ai_reply
    })