import os
import pathlib
import google.generativeai as genai

from utils import resize_image

genai.configure(api_key=os.environ["API_KEY"])
system_instruction = """
    당신은 환경보호 컨텐츠 검수자입니다. 
    사진과 설명을 입력 받으면, 아래와 같이 json 포맷으로 응답합니다.
    {"descr": str, "is_matched": bool, "is_valid": bool, "fail_reason": str}
    descr은 사진에 대한 2줄 이내의 설명(당신이 작성한 설명)이고,
    is_matched는 입력받은 설명이 사진에 대한 설명이 맞는지 여부이고,
    is_valid는 입력받은 사진이 아래 기준에 부합하는지 여부입니다.(적어도 하나 이상의 기준에 부합하면 true 입니다.)
    fail_reason은 is_matched 또는 is_valid가 false일때, 그 이유입니다.(is_matched와 is_valid가 모두 true일 경우, 빈값입니다.)

    [기준]
    - 플라스틱 등의 일회용품을 사용하지 않습니다.
    - 에너지를 절약합니다.
"""
model=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction,
    generation_config={"response_mime_type": "application/json"})

filename = 'breakfast.jpeg'
resize_image(filename, filename, 500)

target_picture = {
    'mime_type': 'image/jpeg',
    'data': pathlib.Path(filename).read_bytes()
}
prompt = "일회용품을 사용하지 않고 아침식사를 준비했습니다."

response = model.generate_content(
    contents=[prompt, target_picture]
)
print(response.text)

"""
[응답]

{"descr": "베이글과 크림치즈, 그리고 텀블러에 담긴 음료로 구성된 간단한 아침 식사입니다.", "is_matched": true, "is_valid": true, "fail_reason": ""}
"""