from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Bot')
treinar = ListTrainer(bot)

for _file in os.listdir("chats"):# percorrer os arquivos do chat
    lines = open("chats/" + _file, "r").readlines() #ler os arquivos
    treinar.train(lines)


def answer(txt):
    return bot.get_response(txt)
