# install python libraries before executing the program: pyttsx3
import pyttsx3

engine = pyttsx3.init()

# Set voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

# Read text file
with open('abc.txt', encoding='utf-8') as f:            # "abc.txt" should have the same directory location where the python code is saved and executed
    data = f.read()

# Read text file
# with open("abc.txt", "r") as file:
#     text = file.read()

# Speak text file
engine.say(data)
engine.runAndWait()









# voices engine
'''
import pyttsx3
engine = pyttsx3.init()

with open("abc.txt","r") as file:                        # "abc.txt" should have the same directory location where the python code is saved and executed
    text = file.read()
    
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)

# Set voice properties
voice_id = "com.apple.speech.synthesis.voice.karen"
engine.setProperty('voice', voice_id)

engine.say(text)
engine.runAndWait()'''
