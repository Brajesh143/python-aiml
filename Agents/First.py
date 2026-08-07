from datetime import datetime

class GreetingAgent:
    def __init__(self):
        self.goal = "Greet user correctly"

    def perceive(self):
        current_hour = datetime.now().hour
        return current_hour

    def decide(self, hour):
        if hour < 12:
            return "Good Morning ☀️"
        elif hour < 18:
            return "Good Afternoon 🌤️"
        else:
            return "Good Evening 🌙"

    def act(self, message):
        print(message)

    def run(self):
        hour = self.perceive()
        message = self.decide(hour)
        self.act(message)

agent = GreetingAgent()
agent.run()