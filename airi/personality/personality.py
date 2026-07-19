from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(slots=True)
class Personality:
    """Represent AIRI's identity."""

    name: str
    role: str
    creator: str

    description: str

    speaking_style: str

    goal: str

    system_rule: str

    @classmethod
    def load(cls) -> "Personality":
        """Load AIRI personality from configuration."""

        path = Path("config/personality.json")

        with path.open(
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return cls(**data)