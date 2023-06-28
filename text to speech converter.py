import pyttsx3

engine = pyttsx3.init()


# Set voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 150)

with open('evm.txt', encoding='utf-8') as f:
    data = f.read()

# Read text file
# with open("zigbee.txt", "r") as file:
#     text = file.read()

# Speak text file
engine.say(data)
engine.runAndWait()







# string statement to speech converter

'''import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here

text = 'XBee is a brand of wireless communication modules manufactured by Digi International. The XBee series includes a variety of different wireless communication protocols, including Zigbee, which is a low-power, low-data-rate wireless communication protocol that is commonly used for wireless sensor networks and home automation systems. Zigbee is a wireless communication protocol that is designed for low-power, low-data-rate applications, and it operates on the IEEE 802.15.4 standard. Zigbee provides secure and reliable wireless communication between devices, and it is commonly used in home automation, industrial automation, and smart energy applications.The Zigbee MG2455 is a specific type of Zigbee module manufactured by Telit. It is designed to provide wireless communication between devices over short distances, typically within a range of 100 meters or less. The MG2455 module is designed for use in a wide range of applications, including industrial automation, building automation, and smart energy applications.In summary, the main difference between the XBee series Zigbee and the Zigbee MG2455 is that the former is a family of wireless communication modules that support the Zigbee protocol, while the latter is a specific Zigbee module manufactured by Telit. Both are designed for low-power, low-data-rate wireless communication applications, and are commonly used in industrial automation, home automation, and smart energy applications.'
engine.say(text)
engine.runAndWait()
'''





# final text to speech
'''

import pyttsx3

engine = pyttsx3.init()

# Set voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

with open('zigbee.txt', encoding='utf-8') as f:
    data = f.read()

# Read text file
# with open("zigbee.txt", "r") as file:
#     text = file.read()

# Speak text file
engine.say(data)
engine.runAndWait()'''





# voices engine
'''
import pyttsx3
engine = pyttsx3.init()

with open("zigbee.txt","r") as file:
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
