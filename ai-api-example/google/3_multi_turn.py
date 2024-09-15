import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

response = chat.send_message("Pretend you\'re a snowman and stay in character for each response.")
print(response.text)
"""
[응답]

Brrr! Hello there!  What brings you to my snowy domain?  Is it the cold that got you, or are you just here to admire my frosty masterpiece? 😄 
"""

response = chat.send_message("What\'s your favorite season of the year?")
print(response.text)
"""
[응답]

Well, that's a no-brainer!  It's gotta be winter, of course!  I mean, I'm a snowman, after all!  What else would I say?  ❄️ 

Though, I do have to admit, the spring can be pretty nice, too.  All that melting snow makes for a nice refreshing drink! 😜
"""