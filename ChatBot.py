import random

class Chatbot:
    def __init__(self):
        self.rules = {
            'greet': ['hello', 'hi', 'hey'],
            'ask_name': ['your name', 'who are you'],
            'ask_weather': ['weather today', 'is it raining'],
            'goodbye': ['goodbye', 'bye', 'see you'],
            'default': ['i don\'t understand', 'can you repeat']
        }
        self.responses = {
            'greet': ['Hello!', 'Hi there!'],
            'ask_name': ['I am Chatbot.', 'Call me Chatbot.'],
            'ask_weather': ['I can\'t check weather.', 'No weather data.'],
            'goodbye': ['Bye!', 'See you later!'],
            'default': ['Sorry, I didn\'t get that.', 'Try asking differently.']
        }

    def respond(self, user_input):
        user_input = user_input.lower()
        for intent, keywords in self.rules.items():
            if any(keyword in user_input for keyword in keywords):
                return random.choice(self.responses[intent])
        return random.choice(self.responses['default'])

# Start the chat
bot = Chatbot()
print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if 'bye' in user_input.lower():
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", bot.respond(user_input))
