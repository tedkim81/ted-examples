import base64
import requests
import os

# OpenAI API Key
api_key = os.environ.get("OPENAI_API_KEY")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to target image. This image was created by running 4_image_generation.py.
image_path = "4_image_generation_result1.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())

"""
[응답]

{
  'id': 'chatcmpl-9eXxyWWkNDKJV1vWulgGBQLN6F9B2', 
  'object': 'chat.completion', 
  'created': 1719450714, 
  'model': 'gpt-4o-2024-05-13', 
  'choices': [{
    'index': 0, 
    'message': {
      'role': 'assistant', 
      'content': 'The image shows two Siamese cats standing close to each other. They have striking blue eyes and characteristic dark coloration on their ears, faces, paws, and tails, which is typical of the Siamese breed. The cats are positioned against a plain white background.'
    }, 
    'logprobs': None, 
    'finish_reason': 'stop'
  }], 
  'usage': {'prompt_tokens': 778, 'completion_tokens': 52, 'total_tokens': 830}, 
  'system_fingerprint': 'fp_4008e3b719'
}
"""