
# string statement to speech converter

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here

text = 'Elon Musk is the founder, chairman, CEO, and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation.'
engine.say(text)
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

