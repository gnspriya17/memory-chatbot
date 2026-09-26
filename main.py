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
    elif question.lower() == "history":
        print("\n----Conversation History----")
        for msg in message:
            if msg["role"] == "user":
                print("You: " + msg["content"])
            elif msg["role"] == "assistant":
                print("Synora:"+ msg["content"])
            print("----------------------------\n")
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
        print("Synora: ", answer)