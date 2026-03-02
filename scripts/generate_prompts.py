with open("data/script.txt", "r", encoding="utf-8") as f:
    script = f.read()

prompts = """
STYLE:
Cute political caricature, bold outlines, flat colors, expressive faces

SCENE 1:
Cartoon narrator explaining world news with floating flags

SCENE 2:
Caricature of Iran, Israel, USA leaders arguing, exaggerated emotions

SCENE 3:
World map reacting, people watching phones anxiously
"""

with open("data/prompts.txt", "w", encoding="utf-8") as f:
    f.write(prompts.strip())

print("✅ Image prompts generated")
