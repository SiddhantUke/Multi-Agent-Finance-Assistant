import whisper
# !pip install gTTS
from gtts import gTTS
import os

asr = whisper.load_model("base")

def speech_to_text(audio_path):
    result = asr.transcribe(audio_path)
    return result['text']

def text_to_speech(text, out_path="output.mp3"):
    tts = gTTS(text)
    tts.save(out_path)
    os.system(f"start {out_path}")