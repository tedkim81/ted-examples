import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])
# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Write a story about a magic backpack.")
print(response.text)

"""
[응답]

Elara, a ten-year-old with a penchant for adventure and a nose for trouble, stumbled upon the backpack in the dusty attic of her grandmother's house. It was an ordinary-looking rucksack, brown leather and worn with age, except for one peculiar detail: a single, iridescent feather woven into the strap. 

The moment Elara touched it, a strange tingling ran up her arm. Curiosity bubbling, she strapped it on. And then, the magic began. 

The attic, once a cavern of forgotten trinkets, transformed into a sun-dappled meadow. Birdsong filled the air, and a playful breeze rustled the tall grass. Elara, wide-eyed, reached out and touched a delicate butterfly, its wings shimmering like stained glass.

"This is amazing!" she whispered, her heart pounding with exhilaration. 

She spent the day exploring enchanted landscapes, meeting talking animals, and learning the secrets of the ancient forest. With every step, the backpack seemed to morph into whatever was needed: a diving suit for exploring coral reefs, a pair of wings for soaring through clouds, even a tiny sailboat for navigating a shimmering lake.

But, as the day waned, a strange unease settled over Elara. The magic felt… off. The vibrant colours of the meadow dimmed, the birdsong grew distant, and the once-playful breeze now felt cold and damp. 

Suddenly, she found herself back in the dusty attic, the backpack now heavy and cold. Panic gripped her. "What happened?" she cried, shaking the bag. 

A deep, rumbling voice echoed from within, "You have disturbed the balance, child. Your eagerness has drained the magic."

Elara, terrified, fumbled with the buckles, desperate to undo the spell. The voice spoke again, "The magic is not yours to control. It is a gift, but a fragile one. It thrives on respect, not reckless abandon."

Elara's heart ached. She understood. The magic had been a breathtaking experience, but she had treated it like a toy, not a gift.

With a heavy sigh, she placed the backpack on the floor. "I'm sorry," she whispered, "I didn't mean to…"

The voice softened, "It's not too late. You have learned a valuable lesson. The magic will return, but only when you are ready to cherish it, not exploit it."

Elara left the attic, the backpack a heavy reminder of her mistake. But she knew, deep down, that she would be ready again. She had tasted the magic, and she wouldn't let it escape her grasp. She would learn to respect its power, to cherish its wonders, and to become a worthy keeper of its secrets. The journey had just begun.
"""