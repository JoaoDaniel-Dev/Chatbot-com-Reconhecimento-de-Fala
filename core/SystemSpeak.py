import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty("voices")

engine.setProperty("voice", voice[1].id)
engine.setProperty("rate", 170)


def speak(txt):
    engine.say(txt)
    engine.runAndWait()
