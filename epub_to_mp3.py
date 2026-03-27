# install required libraries before running:
#   pip install ebooklib==0.18 beautifulsoup4==4.12.3 pyttsx3==2.90

import warnings
import os
import pyttsx3
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup                  # ✅ strips HTML tags before TTS reads them


# ── Get input file from user ─────────────────────────────────
filepath = input("Enter the path to your EPUB file:\n> ").strip()

if not os.path.isfile(filepath):
    print(f"❌ File not found: '{filepath}'. Check the path and try again.")
    exit()

if not filepath.lower().endswith(".epub"):
    print("❌ This script only accepts .epub files.")
    exit()


# ── Extract text from EPUB ───────────────────────────────────
print("📖 Reading EPUB file...")
try:
    warnings.filterwarnings("ignore", category=UserWarning)
    book = epub.read_epub(filepath)
    warnings.resetwarnings()
except Exception as e:
    print(f"❌ Could not open EPUB file: {e}")
    exit()

text = ""
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        raw_html = item.get_content().decode("utf-8")
        soup = BeautifulSoup(raw_html, "html.parser")   # ✅ strips tags so they aren't spoken aloud
        text += soup.get_text(separator=" ") + "\n"

if not text.strip():
    print("⚠ No readable text found in this EPUB. Cannot generate audio.")
    exit()

print(f"  ✅ Extracted ~{len(text.split()):,} words.")


# ── Convert text to MP3 ──────────────────────────────────────
output_filename = os.path.splitext(os.path.basename(filepath))[0] + ".mp3"
output_path = os.path.join(os.path.dirname(filepath), output_filename)

print(f"🔊 Converting to audio...")
try:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 130)     # speaking rate in words per minute
    engine.setProperty("volume", 0.8)   # volume (0.0 to 1.0)

    engine.save_to_file(text, output_path)
    engine.runAndWait()
except Exception as e:
    print(f"❌ Audio conversion failed: {e}")
    exit()

print(f"✅ Done! Saved as: {output_path}")
