from dataclasses import dataclass
from pathlib import Path
import json


@dataclass(slots=True)
class Relationship:
    user_name: str
    ai_name: str
    user_role: str
    ai_role: str
    greeting: str

    @classmethod
    def load(cls) -> "Relationship":
        path = Path("config/relationship.json")

        with path.open(encoding="utf-8") as file:
            data = json.load(file)

        return cls(**data)