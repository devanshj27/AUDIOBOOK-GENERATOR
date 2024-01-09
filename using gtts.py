import PyPDF2

pdf_dir = "VIDEOS/E lockheart - We were liars.pdf"

text = ''

with open(pdf_dir, 'rb') as pdf_file:
    pdf_reader_1 = PyPDF2.PdfReader(pdf_file)

    for page_number in range(14,16):
        page = pdf_reader_1.pages[page_number]
        text += page.extract_text()



from gtts import gTTS

#tts = gTTS(text)
tts = gTTS(text, lang='en', tld = 'co.in')
tts.save("test_gtts.mp3")
