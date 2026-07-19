from airi.app import App
from airi.brain import Brain, DummyLLM
from airi.memory import MemoryManager
from airi.personality import Personality
from airi.prompts import Prompts
from airi.relationship import Relationship
from airi.settings import Settings
from airi.stt.listener import Listener

class Airi:
    def __init__(self):

        # Application
        self.app = App.load()

        # Identity
        self.personality = Personality.load()
        self.relationship = Relationship.load()

        # Prompts
        self.prompts = Prompts.load()

        # Settings
        self.settings = Settings.load()

        # AI Engine
        self.llm = DummyLLM()

        # Core Modules
        self.memory = MemoryManager()
        self.listener = Listener()

        # Brain
        self.brain = Brain(
            personality=self.personality,
            relationship=self.relationship,
            llm=self.llm,
        )

    def introduce(self):
        print(f"🌸 {self.prompts.greeting}")
        print(f"Namaku {self.personality.name}.")
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