import PyPDF2

pdf_dir = "VIDEOS/E lockheart - We were liars.pdf"

text = ''

with open(pdf_dir, 'rb') as pdf_file:
    pdf_reader_1 = PyPDF2.PdfReader(pdf_file)

    for page_number in range(14,16):
        page = pdf_reader_1.pages[page_number]
        text += page.extract_text()

import pyttsx3

# Initialize the pyttsx engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Set the properties for the audio file (optional)
engine.setProperty('rate', 150)   # Set the speaking rate (words per minute)
engine.setProperty('volume', 0.8) # Set the volume (0 to 1)

# Convert the text to speech
engine.save_to_file(text, 'test3.mp3')
engine.runAndWait()



### below code runs on older PyPDF2 library, and does not support the new one
#
# import PyPDF2
#
# pdf_dir = "kaufman2013.pdf"
#
# text = ''
#
# with open(pdf_dir, 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#
#     for page_number in range(1,pdf_reader_1.numPages):
#         page = pdf_reader_1.getPage(page_number)
#         text += page.extractText()
#
# import pyttsx3
#
# engine = pyttsx3.init()
# engine.save_to_file(text, 'test1.mp3')
# engine.runAndWait()