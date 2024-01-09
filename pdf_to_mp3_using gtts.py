import PyPDF2

pdf_dir = "VIDEOS/E lockheart - We were liars.pdf"

text = ''

with open(pdf_dir, 'rb') as pdf_file:
    pdf_reader_1 = PyPDF2.PdfReader(pdf_file)

    # for page_number in range(14,16):                      # un-comment this for loop, here you can specify the page numbers/ range of page numbers you wish to convert to your audio-file
    #     page = pdf_reader_1.pages[page_number]
    #     text += page.extract_text()

    for page_number in range(1,pdf_reader_1.numPages):         # use this for loop if you wish to convert the whole pdf into your audio file.
        page = pdf_reader_1.pages[page_number]
        text += page.extract_text()

from gtts import gTTS

#tts = gTTS(text)
tts = gTTS(text, lang='en', tld = 'co.in')
tts.save("output_gtts.mp3")
