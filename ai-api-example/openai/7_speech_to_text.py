from openai import OpenAI
client = OpenAI()

audio_file= open("6_text_to_speech_result.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcription.text)

"""
[응답]

Today is a wonderful day to build something people love.
"""