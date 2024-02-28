import re
from typing import List


class ChatBot:
    def make_reply(self, text: str) -> str:
       
        matcher = {
            r"\b(hi|hello|hey|what's up)\b": 'Hey bud how are you doing?! Are you ready to cook for me?',
            r"(?i)^how can i become a go{2}d chef\??$":"If you want to become a great chef, you have to work with great chefs. And that's exactly what I did.",
            r"(?i)\bhow(?:'s| is)?(?:\s+(?:it\s+going|are\s+(?:you|things)|you\s+doing|is\severything))?\b":'I am hungry as a Horse, Why dont we cook something!',
            r"\b(sure|ok|yes)\b": 'Alright then, let\'s get cooking.',
            r"\b(?:.*(?:think|like|love).*?(?:pizza|spaghetti|ravioli|pasta|sandwich).*)\b": 'This isn’t a food!! this is a mistake. This is an Italian tragedy!',
            r"\b([0-9]+)\s*(?:\w+\s+)*eggs\b": 'If you put {} eggs, then all the chickens from chicken run are going to think you are Miss Tweedy.',
            r"(?i)\b(?:what\s+can\s+I\s+cook\s+for\s+you|what\s+should\s+I\s+prepare\s+for\s+you|what\s+do\s+you\s+want\s+to\s+eat)\b":'Why dont you cook me some Italian food!',
            r"(?i)\blove\s+your\b":'I’d like to think I’m a great teacher,and definitely am a great cook. Just keep practicing, and one day you might be like me.',
            r"(?i)\b(bye|see\s+(you|ya)(\s+later)?|talk\s+to\s+(you|ya)(\s+later)?)\b": 'Alright bud, talk to you later. It was fun roasting you and cooking with you.'

        }

        for pattern_match, reply in matcher.items():
            found_match = re.search(pattern_match, text.lower())
            if found_match:
                if '{}' in reply:
                    return reply.format(*found_match.groups())
                else:
                    return reply

        # If no match is found, return a default response
        return "OKKKKKK I am making a steak, so let's just talk about cooking?"
        """
        The method where you do your regular expression work!

        Args:
            text (str): the text of the message sent

        Returns:
            str: the chatbot's response
        """
        raise NotImplementedError

    @staticmethod
    def get_name() -> str:
        return 'Chef-ramsey'
        raise NotImplementedError

    @staticmethod
    def examples() -> List[str]:
        example=['What would you like me to cook for you?','What do you think of this pizza(or any Italian food) I made?!!!','I have to say, I love your food and your cooking videos','How can I become a good chef?','Are 8 eggs good enough for the pasta','Bye']
        """
        gives some examples of how your chatbot should be run

        Returns:
            List[str]: _description_
        """
        return example
        raise NotImplementedError


def get_user_statement() -> str:
    """
    Get user input and normalizes it by stripping whitespace and
    converting to lowercase

    Returns:
        str: normalized string from standard input
    """
    return input("you: ").lower().strip()


def main():
    bot = ChatBot()

    print(f"You're chatting with {bot.get_name()}")
    you_said = get_user_statement()
    while you_said.lower().strip() != "exit":
        if you_said == "examples":
            print("Examples: ", bot.examples())
        else:
            bot_said = bot.make_reply(you_said)
            print("bot: " + bot_said)
        you_said = get_user_statement()
    print("Bye!")


if __name__ == "__main__":
    main()

# Discover NLP course materials authored by Julie Medero, Xanda Schofield, and Richard Wicentowski
# This work is licensed under a Creative Commons Attribution-ShareAlike 2.0 Generic License# https://creativecommons.org/licenses/by-sa/2.0/