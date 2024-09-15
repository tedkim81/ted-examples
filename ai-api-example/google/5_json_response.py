import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel(
  'gemini-1.5-flash', 
  generation_config={"response_mime_type": "application/json"}
)

prompt = """
    List 5 popular cookie recipes.

    Using this JSON schema:

    Recipe = {"recipe_name": str}

    Return a `list[Recipe]`
    """

response = model.generate_content(prompt)
print(response)

"""
[응답] (전체 구조 보고 싶어서 response를 출력)

response:
GenerateContentResponse(
    done=True,
    iterator=None,
    result=glm.GenerateContentResponse({
      "candidates": [
        {
          "content": {
            "parts": [
              {
                "text": "[{\"recipe_name\": \"Chocolate Chip Cookies\"}, {\"recipe_name\": \"Oatmeal Raisin Cookies\"}, {\"recipe_name\": \"Snickerdoodles\"}, {\"recipe_name\": \"Sugar Cookies\"}, {\"recipe_name\": \"Peanut Butter Cookies\"}]\n"
              }
            ],
            "role": "model"
          },
          "finish_reason": 1,
          "index": 0,
          "safety_ratings": [
            {
              "category": 9,
              "probability": 1,
              "blocked": false
            },
            {
              "category": 8,
              "probability": 1,
              "blocked": false
            },
            {
              "category": 7,
              "probability": 1,
              "blocked": false
            },
            {
              "category": 10,
              "probability": 1,
              "blocked": false
            }
          ],
          "token_count": 0,
          "grounding_attributions": []
        }
      ]
    }),
)
"""