from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import pyttsx3

bot = ChatBot('Bot')
treinar = ListTrainer(bot)

for _file in os.listdir("chats"):# percorrer os arquivos do chat
    lines = open("chats/" + _file, "r").readlines() #ler os arquivos
    treinar.train(lines)

engine = pyttsx3.init()
voice = engine.getProperty("voices")

engine.setProperty("voice", voice[1].id)
engine.setProperty("rate", 170)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)

    if float(resposta.confidence) >= 0.5:
        print('Bot: ', resposta)

        engine.say(resposta)
        engine.runAndWait()
    else:
        print('Bot: Ainda não sei responder esta pergunta')
        engine.say("Ainda não sei responder esta pergunta")
        engine.runAndWait()
