import json

with open("data/news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

article = news[0]

script = f"""
HOOK:
"Why is the world watching Iran, Israel, and the US right now?"

SCENE 1:
Explain simply: {article['summary']}

SCENE 2:
Cartoon characters of world leaders reacting emotionally.

SCENE 3:
Why this matters to normal people around the world.

ENDING:
"Follow for simple explanations of world news."
"""

with open("data/script.txt", "w", encoding="utf-8") as f:
    f.write(script.strip())

print("✅ Script written")
