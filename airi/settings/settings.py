from dataclasses import dataclass
from pathlib import Path
import json


@dataclass(slots=True)
class Settings:
    """Runtime settings for AIRI."""

    debug: bool
    auto_save_diary: bool
    voice_enabled: bool
    memory_enabled: bool
    theme: str

    @classmethod
    def load(cls) -> "Settings":
        path = Path("config/settings.json")

        with path.open(encoding="utf-8") as file:
            data = json.load(file)

        return cls(**data)