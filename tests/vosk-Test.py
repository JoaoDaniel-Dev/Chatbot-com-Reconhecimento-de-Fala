from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model(r'./model')
recognizer = KaldiRecognizer(model, 16000)


cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
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
                print(text)
