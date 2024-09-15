from openai import OpenAI
from typing_extensions import override
from openai import AssistantEventHandler

client = OpenAI()
  
assistant = client.beta.assistants.create(
  name="Math Tutor",
  instructions="You are a personal math tutor. Write and run code to answer math questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)
thread = client.beta.threads.create()
 
class EventHandler(AssistantEventHandler):    
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)
 
while True:
  user_input = input("\n\nuser > ")
  if user_input.lower() in ["exit", "quit"]:
    break

  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_input
  )

  with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Ted Kim. The user has a premium account.",
    event_handler=EventHandler(),
  ) as stream:
    stream.until_done()

"""
[실행 로그]

user > Who are you?

assistant > Hello, Ted Kim! I'm your AI assistant, here to help you with information, tasks, and any questions you might have. How can I assist you today?

user > I need to solve the equation `3x + 11 = 14`. Can you help me?

assistant > Sure, Ted Kim! Let's solve the equation \( 3x + 11 = 14 \).

1. **Subtract 11 from both sides:**
   \[
   3x + 11 - 11 = 14 - 11
   \]
   \[
   3x = 3
   \]

2. **Divide both sides by 3:**
   \[
   x = frac{3}{3}
   \]
   \[
   x = 1
   \]

So, the solution to the equation \( 3x + 11 = 14 \) is \( x = 1 \).

user > Please run the python code. `for i in range(0,3): print('i * 2 = %d' % (i * 2))`

assistant > code_interpreter

# Let's run the provided Python code
output = []
for i in range(0, 3):
    output.append(f'i * 2 = {i * 2}')
output
assistant > Here is the output from the Python code:

```
i * 2 = 0
i * 2 = 2
i * 2 = 4
```

Is there anything else you'd like to do?

user > exit
"""