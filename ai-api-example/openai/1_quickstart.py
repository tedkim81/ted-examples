from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)

"""
[응답]

ChatCompletionMessage(content="In the realm of code, a concept unique,\nLies the power of recursion, subtle and chic.\nA function that calls upon itself to repeat,\nIn a dance of logic, a mesmerizing feat.\n\nA recursive function, like a mirror's reflection,\nRevisiting itself with each invocation.\nBreaking down problems into smaller bits,\nConquering complexities, piece by piece it knits.\n\nWith each recursive call, a new path taken,\nA journey into the unknown, a code unshaken.\nTackling tasks with elegant grace,\nUnraveling mysteries, embracing the chase.\n\nLike a fractal unfolding in infinite grace,\nRecursion embodies a captivating space.\nA loop of self-replication, a tale untold,\nIn the world of programming, a treasure to behold.\n\nSo heed the call of recursion's allure,\nEmbrace its magic, let your code endure.\nIn the depths of logic, let it guide your way,\nA poetic dance of code, forever to stay.", role='assistant', function_call=None, tool_calls=None)
"""