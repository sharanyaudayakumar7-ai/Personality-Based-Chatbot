import random

def savage_response(text):
    responses = [
        f"'{text}'? That’s your villain origin story? 💀",
        f"Oh nooo… anyway 😴 '{text}'",
        f"Skill issue detected: '{text}' 🤡",
        f"You really thought '{text}' was worth saying? 😭",
        f"Breaking news: nobody asked about '{text}' 📰",
        f"'{text}'… and you’re proud of that? 💀",
        f"Even Google can’t fix '{text}' 😬"
    ]
    return random.choice(responses)


def sweet_response(text):
    responses = [
        f"Aww 🥺 '{text}'… you’re doing your best and that’s enough 💖",
        f"It’s okay ❤️ '{text}' doesn’t define you",
        f"Sending hugs 🤗 things will get better after '{text}'",
        f"You’re stronger than '{text}' 💪✨",
        f"Hey… be kind to yourself 🥺 '{text}' is just a phase"
    ]
    return random.choice(responses)


def sarcastic_response(text):
    responses = [
        f"Oh wow. '{text}'. Absolutely life-changing 🙄",
        f"Groundbreaking. Truly. '{text}' 👏",
        f"Ah yes, '{text}'… peak intelligence right there 🧠",
        f"I'm so impressed by '{text}'… said no one ever 😏",
        f"'{text}'… wow, Nobel Prize incoming 🏆"
    ]
    return random.choice(responses)


def motivational_response(text):
    responses = [
        f"Hey! '{text}' is just the beginning 🚀 Keep pushing!",
        f"Don’t stop! '{text}' is part of your journey 💪",
        f"You got this! '{text}' won’t hold you back 🔥",
        f"Rise above '{text}' and shine ✨",
        f"Every failure like '{text}' builds success 🧠"
    ]
    return random.choice(responses)