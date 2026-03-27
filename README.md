# 📚 Audiobook Generator

Convert any readable document into audio — right from your terminal.  
Built to help people with reading difficulties, or anyone who prefers listening over reading.

---

## 🗂 Scripts Overview

### 1. `epub_to_mp3.py`
Converts an **EPUB** e-book file into an **MP3** audio file.

- Strips HTML tags from the EPUB content before reading (so tags like `<p>` are never spoken aloud)
- Saves the MP3 in the same folder as your EPUB, using the same filename
- Uses your system's built-in voice engine (works offline)

**Requires:**
```
pip install ebooklib==0.18 beautifulsoup4==4.12.3 pyttsx3==2.90
```

---

### 2. `pdf_to_mp3.py`
Converts a **PDF** file into an **MP3** audio file.

- Reads all pages of the PDF and extracts the text
- Warns you if any page has no extractable text (e.g. scanned/image-only pages)
- Saves the MP3 in the same folder as your PDF, using the same filename
- Uses your system's built-in voice engine (works offline)

**Requires:**
```
pip install PyPDF2==3.0.1 pyttsx3==2.90
```

---

### 3. `pdf_to_mp3_using_gtts.py`
Converts a **PDF** file into an **MP3** audio file using **Google Text-to-Speech (gTTS)**.

- Same PDF reading behaviour as `pdf_to_mp3.py`
- Uses Google's TTS engine instead — sounds more natural and human-like
- Saves the MP3 in the same folder as your PDF, using the same filename
- ⚠️ Requires an active **internet connection**

**Requires:**
```
pip install PyPDF2==3.0.1 gTTS==2.5.1
```

---

### 4. `string_to_speech_converter.py`
Speaks a **block of text** you type directly into the terminal.

- No file needed — just type or paste your text when prompted
- Plays the audio immediately; does **not** save an MP3
- Good for quickly listening to a short passage or testing your voice settings
- Uses your system's built-in voice engine (works offline)

**Requires:**
```
pip install pyttsx3==2.90
```

---

### 5. `txt-file_to_speech.py`
Reads a **plain text (.txt) file** aloud through your speakers.

- Plays the audio immediately; does **not** save an MP3
- Useful for proofreading your own writing by ear
- Uses your system's built-in voice engine (works offline)

**Requires:**
```
pip install pyttsx3==2.90
```

---

## ⚡ Quick Start

1. Install the libraries for the script you want to use (see above)
2. Run the script:
   ```
   python epub_to_mp3.py
   ```
3. When prompted, enter the full path to your file
4. Wait for the ✅ confirmation — your audio file will be ready!

---

## 🗺 Roadmap

- [ ] Unified single-script launcher with a format menu
- [ ] GUI / desktop interface (planned with `tkinter`)
- [ ] Support for more formats (DOCX, HTML, etc.)
- [ ] Voice and speed selection at runtime

---

## 🛠 Troubleshooting

| Problem | Likely Cause | Fix |
|---|---|---|
| `❌ File not found` | Path typed incorrectly | Copy-paste the full file path |
| Page has no extractable text | PDF is scanned / image-based | Try an OCR tool first (e.g. Adobe Acrobat) |
| gTTS fails | No internet connection | Switch to `pdf_to_mp3.py` (offline) |
| Wrong voice speaking | `voices[1]` not available on your system | Change the index to `voices[0]` in the script |
| Audio sounds cut off | File is very large | Be patient — large files take longer to process |

---

## 📬 Contributing

Tips, suggestions, and pull requests are welcome!  
A beginner-friendly UI is the next big goal — ideas appreciated.
