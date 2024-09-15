from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What are in these images? Is there any difference between them?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
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
print(response.choices[0])

"""
[응답]

Choice(
  finish_reason='stop', 
  index=0, 
  logprobs=None, 
  message=ChatCompletionMessage(
    content='The two images are identical. They both depict a wooden boardwalk leading through a grassy field under a blue sky with scattered clouds. The boardwalk stretches into the distance, flanked by tall grasses and some bushes. The landscape is open, and the lighting suggests it is a bright day. There are no differences between the two images; they are the same.', 
    role='assistant', 
    function_call=None, 
    tool_calls=None
  )
)
"""