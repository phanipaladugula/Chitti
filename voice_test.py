from voice_stt import speech_to_text
from voice_tts import text_to_speech
from agent import get_reply

audio_file="sample.wav"

text=speech_to_text(audio_file)
print("User: ",text)

reply=get_reply(text)
print("AI: ",reply)

out=text_to_speech(reply)
print("Audio Generated: ",out)

