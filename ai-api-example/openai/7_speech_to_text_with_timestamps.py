from openai import OpenAI
client = OpenAI()

audio_file = open("6_text_to_speech_result.mp3", "rb")
transcript = client.audio.transcriptions.create(
  file=audio_file,
  model="whisper-1",
  response_format="verbose_json",
  timestamp_granularities=["word"]
)

print(transcript.words)

"""
[응답]

[
  {'word': 'Today', 'start': 0.0, 'end': 0.2800000011920929}, 
  {'word': 'is', 'start': 0.2800000011920929, 'end': 0.46000000834465027}, 
  {'word': 'a', 'start': 0.46000000834465027, 'end': 0.6000000238418579}, 
  {'word': 'wonderful', 'start': 0.6000000238418579, 'end': 0.9399999976158142}, 
  {'word': 'day', 'start': 0.9399999976158142, 'end': 1.2000000476837158}, 
  {'word': 'to', 'start': 1.2000000476837158, 'end': 1.4199999570846558}, 
  {'word': 'build', 'start': 1.4199999570846558, 'end': 1.5399999618530273}, 
  {'word': 'something', 'start': 1.5399999618530273, 'end': 1.8600000143051147}, 
  {'word': 'people', 'start': 1.8600000143051147, 'end': 2.200000047683716}, 
  {'word': 'love', 'start': 2.200000047683716, 'end': 2.5199999809265137}
]
"""