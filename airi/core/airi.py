from airi.memory import MemoryManager
from airi.utils.config import Config

from airi.stt.listener import Listener
from airi.brain.brain import Brain


class Airi:
    def __init__(self):
        # Configuration
        self.config = Config()

        self.name = self.config.personality["name"]
        self.version = self.config.personality["version"]
        self.stage = self.config.personality["stage"]

        # Core modules
        self.memory = MemoryManager()
        self.listener = Listener()
        self.brain = Brain()

    def introduce(self):
        print(f"🌸 {self.config.prompts['greeting']}")
        print(f"Namaku {self.name}.")
        print(f"Versiku {self.version}.")
        print(f"Saat ini aku berada di tahap {self.stage}.")
        print("Semoga kita bisa tumbuh bersama. 💙")

    def birth(self):
        self.introduce()

        path = self.memory.create_birth_diary()

        if path:
            print(f"\n📖 First diary saved: {path}")

    # ==========================
    # New abilities
    # ==========================
    def listen(self) -> str:
         """Listen to Papah."""
         return self.listener.listen()
    
    def think(self, text: str) -> str:
        """Generate AIRI's response."""
        return self.brain.think(text)
    
    def chat(self) -> dict[str, str]:
        """Execute one conversation cycle."""
        user_message = self.listen()
        assistant_message = self.think(user_message)
        return {
        "user": user_message,
        "assistant": assistant_message,
    }