from dataclasses import dataclass
from pathlib import Path
import json


@dataclass(slots=True)
class Prompts:
    """Frequently used prompts for AIRI."""

    greeting: str
    farewell: str
    thinking: str

    @classmethod
    def load(cls) -> "Prompts":
        path = Path("config/prompts.json")

        with path.open(encoding="utf-8") as file:
            data = json.load(file)

        return cls(**data)