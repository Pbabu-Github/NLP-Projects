# Chef Ramsey Bot

A playful chatbot inspired by Gordon Ramsay that loves to roast your cooking skills! This project uses simple **regular expressions** to detect user input and reply with cooking-themed banter.

---

## Features
- Responds to greetings, cooking questions, and food talk.
- Roasts bad Italian food choices (like pizza or spaghetti mistakes).
- Makes fun of you if you try to use too many eggs.
- Provides cooking-themed conversations in the style of Chef Ramsay.

---

## How It Works
The chatbot uses Python's `re` module to match user input against a set of predefined patterns. Each pattern has a corresponding response, so when a user types a message that matches a pattern, the bot replies with the appropriate text. If no patterns match, the bot gives a default cooking-related response.

---

## Installation
Clone the repository:
```bash
git clone https://github.com/your-username/chef-ramsey-bot.git
cd chef-ramsey-bot
```
Run the chatbot:
```bash
python chatbot.py
```
Example Usage:

You're chatting with Chef-ramsey
you: hi
bot: Hey bud how are you doing?! Are you ready to cook for me?

you: how can I become a good chef?
bot: If you want to become a great chef, you have to work with great chefs. And that's exactly what I did.

you: I love your food!
bot: I’d like to think I’m a great teacher,and definitely am a great cook. Just keep practicing, and one day you might be like me.

you: 8 eggs
bot: If you put 8 eggs, then all the chickens from chicken run are going to think you are Miss Tweedy.

Commands

Type examples to see sample prompts.

Type exit to quit the chatbot.
