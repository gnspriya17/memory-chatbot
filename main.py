from ollama import chat

print("Synora - A chatbot that remembers your conversations and provides personalized responses.")
message = []
message.append({
    "role": "system",
    "content": "Answer in a sentence of around 50 words."
})

while True:
    question = input("You: ").strip()
    if question.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    else:
        message.append({
            "role": "user",
            "content": question
        })
        response = chat(model="gemma3:1b", messages=message)
        answer = response.message.content
        message.append({
            "role": "assistant",
            "content": answer
        })
        print("Synora:", answer)