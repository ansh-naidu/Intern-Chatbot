import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chatbot(question: str, context: str = "") -> str:
    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": "You are InternIQ Bot helping with intern training queries."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4.0-mini",
        messages=messages,
        max_tokens=150,
        temperature=0.7
    )

    content = response.choices[0].message.content
    return content.strip() if content else "No response received."

if __name__ == "__main__":
    answer = ask_chatbot("Explain REST APIs.")
    print(answer)
