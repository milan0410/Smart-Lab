import pyttsx3
engine=pyttsx3.init()
def announce(annoucement):
    engine.say(annoucement)
    engine.runAndWait()
    