# install required libraries before running:
#   pip install pyttsx3==2.90

import os
import pyttsx3


# ── Get input file from user ─────────────────────────────────
filepath = input("Enter the path to your TXT file:\n> ").strip()

if not os.path.isfile(filepath):
    print(f"❌ File not found: '{filepath}'. Check the path and try again.")
    exit()

if not filepath.lower().endswith(".txt"):
    print("❌ This script only accepts .txt files.")
    exit()


# ── Read text file ────────────────────────────────────────────
print("📖 Reading TXT file...")
try:
    with open(filepath, encoding="utf-8") as f:
        data = f.read()
except Exception as e:
    print(f"❌ Could not read file: {e}")
    exit()

if not data.strip():
    print("⚠ The text file appears to be empty. Nothing to play.")
    exit()

print(f"  ✅ Loaded ~{len(data.split()):,} words.")


# ── Speak the text ────────────────────────────────────────────
print("🔊 Speaking...")
try:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 150)     # speaking rate in words per minute
    engine.say(data)
    engine.runAndWait()
except Exception as e:
    print(f"❌ Could not play audio: {e}")
    exit()

print("✅ Done!")
