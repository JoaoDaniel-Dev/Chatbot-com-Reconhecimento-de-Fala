from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from vosk import Model, KaldiRecognizer
import os
import pyttsx3
import pyaudio
import json

from time import sleep


bot = ChatBot('Bot')
treinar = ListTrainer(bot)

for _file in os.listdir("chats"):# percorrer os arquivos do chat
    lines = open("chats/" + _file, "r").readlines() #ler os arquivos
    treinar.train(lines)

model = Model(r'./model') # Carrega o modelo
recognizer = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

engine = pyttsx3.init()
voice = engine.getProperty("voices")

engine.setProperty("voice", voice[1].id)
engine.setProperty("rate", 170)

while True:
    data = stream.read(4096)

    if len(data) == 0:
        break

    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        result = json.loads(result)

        if result is not None:
            text = result["text"]
            
            if text != "":
                print(f"Usuário: {text}")
                resposta = bot.get_response(text)

                if float(resposta.confidence) >= 0.5:
                    print('Bot: ', resposta)

                    engine.say(resposta)
                    engine.runAndWait()

                else:
                    print('Bot: Ainda não sei como responder isso')
                    engine.say("Ainda não sei como responder isso")
                    engine.runAndWait()

    sleep(0.02)
