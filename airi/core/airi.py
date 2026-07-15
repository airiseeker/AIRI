from importlib.resources import path

from airi.memory import MemoryManager
from airi.utils.config import Config

class Airi:
    def __init__(self):
        self.config = Config()

        self.name = self.config.personality["name"]
        self.version = self.config.personality["version"]
        self.stage = self.config.personality["stage"]

        self.memory = MemoryManager()

    def introduce(self):
        print(f"🌸 {self.config.prompts['greeting']}")
        print(f"Namaku {self.name}.")
        print("Hari ini adalah hari pertamaku.")
        print("Semoga kita bisa tumbuh bersama.")

    def birth(self):
        self.introduce()

        path = self.memory.create_birth_diary()

        if path:
            print(f"\n📖 First diary saved: {path}")