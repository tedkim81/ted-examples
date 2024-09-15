from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
print(response.choices)

"""
[응답]

[
  Choice(
    finish_reason='stop', 
    index=0, 
    logprobs=None, 
    message=ChatCompletionMessage(
      content='This image depicts a picturesque scene of a wooden boardwalk path stretching through a grassy field. The sky is blue with some scattered clouds, and the surrounding vegetation is lush and green, suggesting a summer or late spring setting. Trees and shrubs can be seen in the background, adding to the serene and natural atmosphere of the landscape.', 
      role='assistant', 
      function_call=None, 
      tool_calls=None
    )
  )
]
"""