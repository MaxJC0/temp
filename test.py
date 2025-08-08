import random

emojis = ["😎", "🚀", "🐍", "🎉", "🤖", "🍕", "🧠", "🌈"]
messages = [
    "You're crushing it!",
    "Python power activated!",
    "Time to debug... or dance?",
    "Code like nobody's watching.",
    "One step closer to world domination.",
    "May your syntax be flawless.",
    "AI approves this message.",
    "Keep calm and import random."
]

print(f"{random.choice(emojis)} {random.choice(messages)}")
