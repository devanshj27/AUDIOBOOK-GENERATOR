# install required libraries before running:
#   pip install pyttsx3==2.90

import pyttsx3


# ── Get text input from user ──────────────────────────────────
print("Enter the text you want converted to speech.")
print("(Press Enter twice when done)\n")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = " ".join(lines).strip()

if not text:
    print("❌ No text entered. Please try again.")
    exit()


# ── Speak the text ────────────────────────────────────────────
print("\n🔊 Speaking...")
try:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)   # 0 = first voice, 1 = second voice
    engine.say(text)
    engine.runAndWait()
except Exception as e:
    print(f"❌ Could not play audio: {e}")
    exit()

print("✅ Done!")
