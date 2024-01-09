# install this python library before executing the program: ebooklib, 
# install python libraries before executing the program: pyttsx3

import ebooklib
from ebooklib import epub
import pyttsx3

import warnings
from ebooklib import epub

# Ignore the warning message
warnings.filterwarnings("ignore", category=UserWarning)

book = epub.read_epub('abc.epub')
# "abc" should be the file name of the epub file and this epub file should have the same directory location where the python code is saved and executed

# Restore the warning message filter to its original state
warnings.resetwarnings()

# Open the EPUB file
# book = epub.read_epub('sample_book.epub')
# book = epub.read_epub('sample_book.epub', ignore_missing_ncx=True, ignore_missing_toc=True, ignore_epub=True, ignore_images=True, ignore_ncx=True)

# Extract the text from the book
text = ''
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        text += item.get_content().decode('utf-8')
        #text += item.get_content()

# Initialize the pyttsx engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Set the properties for the audio file (optional)
engine.setProperty('rate', 130)   # Set the speaking rate (words per minute)
engine.setProperty('volume', 0.8) # Set the volume (0 to 1)

# Convert the text to speech
engine.save_to_file(text, 'output_audio.mp3')
# here "output_audio.mp3" is the name of the output file. This output file will get stored and saved in the same directory location where the python code is saved and executed
engine.runAndWait()
