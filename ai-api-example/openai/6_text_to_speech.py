from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "6_text_to_speech_result.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

# stream_to_file() 실행시 deprecated 경고 문구가 출력됩니다.
# response.stream_to_file(speech_file_path)

response.write_to_file(speech_file_path)