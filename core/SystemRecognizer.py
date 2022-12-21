from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r'./model') # Carrega o modelo


def recognizer():
    recognizer = KaldiRecognizer(model, 16000)

    return recognizer


def stream():
    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    return stream
