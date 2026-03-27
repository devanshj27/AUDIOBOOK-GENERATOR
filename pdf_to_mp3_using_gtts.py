# install required libraries before running:
#   pip install PyPDF2==3.0.1 gTTS==2.5.1

import os
import PyPDF2
from gtts import gTTS


# ── Get input file from user ─────────────────────────────────
filepath = input("Enter the path to your PDF file:\n> ").strip()

if not os.path.isfile(filepath):
    print(f"❌ File not found: '{filepath}'. Check the path and try again.")
    exit()

if not filepath.lower().endswith(".pdf"):
    print("❌ This script only accepts .pdf files.")
    exit()


# ── Extract text from PDF ────────────────────────────────────
print("📖 Reading PDF file...")
text = ""

try:
    with open(filepath, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)          # ✅ replaces deprecated .numPages
        print(f"  Found {total_pages} pages.")

        for i, page in enumerate(reader.pages):
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
            else:
                print(f"  ⚠ Page {i+1} had no extractable text (may be image-based).")
except Exception as e:
    print(f"❌ Could not read PDF: {e}")
    exit()

if not text.strip():
    print("⚠ No readable text found in this PDF. Cannot generate audio.")
    exit()

print(f"  ✅ Extracted ~{len(text.split()):,} words.")


# ── Convert text to MP3 using Google TTS ─────────────────────
# Note: gTTS requires an active internet connection
output_filename = os.path.splitext(os.path.basename(filepath))[0] + ".mp3"
output_path = os.path.join(os.path.dirname(filepath), output_filename)

print("🔊 Converting to audio using Google TTS...")
try:
    tts = gTTS(text, lang="en", tld="co.in")
    tts.save(output_path)
except Exception as e:
    print(f"❌ Audio conversion failed: {e}")
    print("   Make sure you have an active internet connection for gTTS.")
    exit()

print(f"✅ Done! Saved as: {output_path}")
