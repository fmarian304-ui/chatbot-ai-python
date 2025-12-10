import random
import time

class AIChatBot:
    def __init__(self):
        self.name = "Aiden"
        self.memory = []

    def slow_print(self, text, delay=0.03):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()

    def add_to_memory(self, user_input, bot_response):
        self.memory.append({"user": user_input, "bot": bot_response})
        if len(self.memory) > 5:  # keep memory short
            self.memory.pop(0)

    def greet(self):
        greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Greetings! Ready when you are."
        ]
        return random.choice(greetings)

    def farewell(self):
        farewells = [
            "Goodbye! Have a great day!",
            "See you soon!",
            "Farewell! Take care!"
        ]
        return random.choice(farewells)

    def unknown(self):
        responses = [
            "I'm not sure I understand. Could you rephrase?",
            "Interesting… tell me more.",
            "Hmm, I didn’t catch that. Try again?"
        ]
        return random.choice(responses)

    def respond(self, user_input):
        text = user_input.lower()

        # Basic intent recognition
        if "hello" in text or "hi" in text:
            response = self.greet()
        elif "your name" in text:
            response = f"My name is {self.name}. I'm your virtual assistant."
        elif "how are you" in text:
            response = "I'm functioning perfectly! How about you?"
        elif "help" in text:
            response = (
                "Sure! Here are some things you can ask me:\n"
                "- 'Tell me a joke'\n"
                "- 'Give me advice'\n"
                "- 'Show memory'\n"
                "- 'Clear memory'\n"
                "- 'Goodbye'"
            )
        elif "joke" in text:
            response = random.choice([
                "Why don’t programmers like nature? Too many bugs!",
                "I tried to catch fog yesterday. Mist!",
                "Debugging: Removing needles from a haystack."
            ])
        elif "advice" in text:
            response = random.choice([
                "Stay consistent. Small daily progress leads to big results.",
                "Failure is knowledge in disguise. Keep going!",
                "If you can’t do it perfectly, do it anyway. Progress > perfection."
            ])
        elif "memory" in text and "show" in text:
            if not self.memory:
                response = "My memory is empty!"
            else:
                response = "Here is what I remember:\n"
                for m in self.memory:
                    response += f"You: {m['user']} | Me: {m['bot']}\n"
        elif "memory" in text and "clear" in text:
            self.memory = []
            response = "Memory cleared successfully!"
        elif "goodbye" in text or "bye" in text:
            response = self.farewell()
        else:
            response = self.unknown()

        self.add_to_memory(user_input, response)
        return response


def main():
    bot = AIChatBot()
    bot.slow_print("=== AIDEN - AI ChatBot ===")
    bot.slow_print("Type 'goodbye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["goodbye", "bye", "exit"]:
            bot.slow_print(bot.farewell())
            break

        bot_response = bot.respond(user_input)
        bot.slow_print("Bot: " + bot_response)


if __name__ == "__main__":
    main()
