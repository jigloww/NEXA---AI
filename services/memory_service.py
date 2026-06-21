class MemoryService:
    def __init__(self):
        self.chat_history = []

    def add_message(self, role, content):
        self.chat_history.append({
            "role": role,
            "content": content
        })

    def get_context(self):
        context = ""

        for message in self.chat_history:
            context += f"{message['role']}: {message['content']}\n"

        return context

    def clear(self):
        self.chat_history = []