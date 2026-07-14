from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Assistant")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

print("🤖 Chatbot is ready! Type 'exit' to quit.")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot.get_response(user)
    print("Bot:", response)