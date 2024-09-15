from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)
print(response.data)

"""
[응답] (실제로는 줄넘김 없이 왔으나, 보기 불편해서 줄넘김은 임의로 추가함)

[
    Image(
        b64_json=None, 
        revised_prompt="A Siamese cat with a predominantly white coat, mesmerizing blue eyes, and distinctive patches of color on its ears, paws, and tail. The cat's tail twitches gently, offering a glint of playfulness. Its ears are pricked up, attuned to the sounds around it. There's a gentle curvature to its body, instilling grace into its posture. The cat's whiskers are perfectly fanned out, adding another layer to its enigmatic expression. All this set against a neutral background, allowing the Siamese cat's beauty to take center stage.", 
        url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-ZQ5PqTcWfZwT9LsBOG5QTvyF/user-5xZtpJEznnG2uBlfoEAezPCA/img-4Uy6oO2a6kF0JT9TKw2D5TXN.png?st=2024-06-26T16%3A31%3A41Z&se=2024-06-26T18%3A31%3A41Z&sp=r&sv=2023-11-03&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-06-25T23%3A15%3A02Z&ske=2024-06-26T23%3A15%3A02Z&sks=b&skv=2023-11-03&sig=D9Or20o3U2BvHO/ZBD3X2fbKU%2BJeqFXLjAOUXn1tD1o%3D'
    )
]
"""