import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(
    "Write a story about a magic backpack.",
    stream=True
)

print(response)
"""
[응답]

GenerateContentResponse(
    done=False,
    iterator=<_StreamingResponseIterator>,
    result=glm.GenerateContentResponse({
      "candidates": [
        {
          "content": {
            "parts": [
              {
                "text": "El"
              }
            ],
            "role": "model"
          },
          "finish_reason": 1,
          "index": 0,
          "safety_ratings": [],
          "token_count": 0,
          "grounding_attributions": []
        }
      ]
    }),
)
"""

for chunk in response:
    print(chunk.text)
    print("_" * 80)

"""
[응답]  (respnose가 모두 완료되지 않은 상태에서도 chunk가 오는대로 바로 출력된다.)

El
________________________________________________________________________________
ara, a girl with eyes as bright as the summer sun and hair the color
________________________________________________________________________________
 of spun wheat, was tired of being ordinary. She yearned for adventure,
________________________________________________________________________________
 for something extraordinary to happen. She dreamt of faraway lands, of talking animals, and of magical creatures. One day, while rummaging through her attic
________________________________________________________________________________
, she stumbled upon a dusty, leather backpack tucked away in a forgotten corner. It was unlike any backpack she'd seen before, adorned with intricate silver carvings
________________________________________________________________________________
 and a worn leather strap that felt strangely warm to the touch.

As Elara unzipped the backpack, a gust of wind swept through the attic, rustling the cobwebs and making the old windows rattle. Inside, nestled amongst the faded
________________________________________________________________________________
 lining, lay a small, shimmering stone. It pulsated with a soft, blue light, and Elara felt an inexplicable pull towards it.  

"What is this?" she whispered, her fingers trembling as she reached for the stone
________________________________________________________________________________
.

As soon as her fingers brushed the stone, the attic was flooded with blinding light. When Elara opened her eyes, she was no longer in the dusty attic, but in a lush, emerald forest. Tall, ancient trees towered over her, their branches interwoven to form a canopy that blocked out the sun
________________________________________________________________________________
. 

Elara gasped, her heart pounding. The backpack, now sitting open beside her, seemed to hum with a faint, magical energy. A voice, soft as the rustle of leaves, echoed in her mind. "Welcome, Elara, to the Enchanted Forest. This backpack is your guide, your
________________________________________________________________________________
 companion, and your key to a world beyond your wildest dreams."

Elara spent the next few days exploring the Enchanted Forest, the backpack seemingly holding an endless supply of tools and necessities. It provided her with a map that glowed with mystical light, revealing hidden pathways and secret waterfalls. It produced delicious meals, fresh fruits
________________________________________________________________________________
, and even a pair of sturdy boots that helped her navigate the treacherous terrain. But the most incredible thing about the backpack was its ability to communicate with animals.  

With the backpack's help, Elara befriended a talking squirrel named Pip, who shared the secrets of the forest, and a wise old owl
________________________________________________________________________________
 named Athena, who taught her the language of the wind. She even encountered a mischievous imp named Flicker, who, despite his mischievous nature, proved to be a valuable friend.

Through the backpack, Elara discovered that she was no ordinary girl. She possessed a hidden talent for magic, an ability that the backpack
________________________________________________________________________________
 nurtured and amplified. She learned to control the elements, to heal with a touch, and to communicate with the spirits of the forest.

But the magic of the backpack came with a price. Elara discovered that its power was not unlimited. She could only use its magic for good, and each time she did,
________________________________________________________________________________
 the stone within the backpack would dim a little. When the stone was completely extinguished, the backpack would lose its magic, and the gateway to the Enchanted Forest would close.

Elara, with the help of her newfound friends, embarked on a series of adventures, using the backpack's magic to help those in need
________________________________________________________________________________
. She rescued a captured phoenix, helped a group of fairies fight off a band of goblins, and even healed a wounded unicorn. With each adventure, the stone in the backpack dimmed a little, but Elara’s courage and compassion grew stronger.

One day, a dark shadow fell over the Enchanted Forest. A
________________________________________________________________________________
 powerful sorcerer, driven by greed and a lust for power, had discovered the magic of the backpack and sought to claim it for his own. He sent his minions to capture Elara and steal the backpack.

With the help of her friends, Elara managed to escape, but the sorcerer was relentless. In a final
________________________________________________________________________________
 showdown, Elara had to choose between using the last of the backpack's magic to save her friends and herself, or to let the sorcerer have his way.

Elara knew what she had to do. She stood tall, her eyes ablaze with courage and determination. She channeled the last of the backpack’s
________________________________________________________________________________
 magic, summoning a powerful wave of energy that repelled the sorcerer and his minions. As the sorcerer vanished, the stone in the backpack finally extinguished, the backpack falling silent and inert.

Elara knew she had to leave the Enchanted Forest, but she was no longer the same girl who had stumbled into its magic. She
________________________________________________________________________________
 had grown stronger, braver, and more compassionate. She carried the lessons she learned in the Enchanted Forest with her, a reminder that even ordinary people can do extraordinary things when they embrace their own inner magic.

As Elara stepped back into the familiar attic, she knew she would never forget the magical journey she had
________________________________________________________________________________
 experienced. The backpack lay empty, but the magic it had bestowed upon her lingered, a secret whispered by the wind, a memory forever etched in her heart. 

________________________________________________________________________________
"""