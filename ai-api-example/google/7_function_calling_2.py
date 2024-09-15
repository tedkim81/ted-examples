import os
import requests
import google.generativeai as genai
from google.generativeai.types import content_types

genai.configure(api_key=os.environ["API_KEY"])

def get_html_text(url: str) -> str:
    """
    Gets HTML text from a given URL.

    Args:
        url: URL to retrieve HTML text from.

    Returns:
        HTML text. If the request fails, it returns None.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML from {url}: {e}")
        return None

system_instruction = 'When you are given a URL, call the get_html_text function to get the html, ' \
    'get og:title, og:image, og:description from that html, find the text, summarize the content as summary, ' \
    'and return the response in json format.\n' \
    '(Example)\n' \
    '{"og:title": str, "og:image": str, "og:description": str, "summary": str}'
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash', 
    tools=[get_html_text],
    system_instruction=system_instruction,
)

prompt = 'https://www.bbc.com/news/articles/c99wg4zz705o'
tool_config = content_types.to_tool_config({"function_calling_config": {"mode": 'AUTO'}})
chat = model.start_chat(enable_automatic_function_calling=True)
response = chat.send_message(prompt, tool_config=tool_config)

print(response.text)

"""
[출력]

```json
{
    "og:title": "Low carbon energy centre proposed for Exeter", 
    "og:image": "https://ichef.bbci.co.uk/news/1024/branded_news/5bb9/live/afe88a70-3eb5-11ef-b74c-bb483a802c97.jpg", 
    "og:description": "Exeter Energy Ltd said the new centre would act as a centralised heat source.", 
    "summary": "An energy company is proposing a low carbon energy centre in Exeter. The centre would be near the Water Lane Solar Park and would use water source heat pumps to take heat from the River Exe. The company plans to apply for planning permission later this year. Two public exhibitions are being held on Thursday and Saturday for residents to learn more about the project."
}
```
"""