import os
import google.generativeai as genai
import pathlib

from utils import resize_image

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# filename = 'breakfast.jpeg'
filename = 'sample_room.jpg'
resize_image(filename, filename, 500)

target_picture = {
    'mime_type': 'image/jpeg',
    'data': pathlib.Path(filename).read_bytes()
}
prompt = "이 사진에 대해 설명해 주세요."

response = model.generate_content(
    contents=[prompt, target_picture]
)
print(response.text)

"""
[breakfast.jpeg에 대한 응답] (실제로는 줄넘김 없이 왔으나, 보기 불편해서 줄넘김은 임의로 추가함)

이 사진은 검은색 트레이에 놓인 몇 가지 음식을 보여줍니다. 
트레이에는 갓 구운 베이글, 작은 접시에 담긴 버터, 컵에 담긴 음료수가 있습니다. 
베이글은 그릇 위에 놓인 칼 옆에 있습니다. 
버터에는 녹색 허브가 뿌려져 있습니다. 
음료는 유리컵에 담겨 있으며 스테인리스스틸 컵으로 둘러싸여 있습니다.

[sample_room.jpg에 대한 응답]

이 사진은 현대적인 가구로 꾸며진 밝고 깨끗한 거실을 보여줍니다. 
거실의 왼쪽에는 창문이 있고, 오른쪽에는 TV가 놓인 엔터테인먼트 센터가 있습니다. 
TV 아래에는 책장이 있고, 바닥에는 털이 덮인 흰색 고양이가 앉아 있습니다. 
바닥은 나무로 되어 있으며, 거실에는 짙은 회색과 베이지색으로 덮여 있습니다.
"""