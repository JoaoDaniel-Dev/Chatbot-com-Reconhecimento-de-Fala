from core import SystemSpeak, SystemChat, SystemRecognizer
import json
from time import sleep

recognizer = SystemRecognizer.recognizer()

stream = SystemRecognizer.stream()
stream.start_stream()

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
                answer = SystemChat.answer(text)

                if float(answer.confidence) >= 0.5:
                    print('Bot: ', answer)
                    SystemSpeak.speak(answer)

                else:
                    print('Bot: Ainda não sei como responder isso')
                    SystemSpeak.speak("Ainda não sei como responder isso")

    sleep(0.03)
