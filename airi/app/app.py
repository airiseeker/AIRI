from dataclasses import dataclass
from pathlib import Path
import json


@dataclass(slots=True)
class App:
    """Application metadata."""

    version: str
    stage: str

    @classmethod
    def load(cls) -> "App":
        path = Path("config/app.json")

        with path.open(encoding="utf-8") as file:
            data = json.load(file)

        return cls(**data)