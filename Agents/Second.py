class TaskAgent:
    def __init__(self):
        self.goal = "Classify user task"

    def perceive(self, task):
        return task.lower()

    def decide(self, task):
        if "code" in task or "program" in task:
            return "This is a CODING task 💻"
        elif "write" in task or "blog" in task:
            return "This is a WRITING task ✍️"
        else:
            return "This is a GENERAL task 📌"

    def act(self, result):
        print(result)

    def run(self, task):
        perceived_task = self.perceive(task)
        decision = self.decide(perceived_task)
        self.act(decision)

agent = TaskAgent()
agent.run("Write a blog on Agentic AI")