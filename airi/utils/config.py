import json
from pathlib import Path
from typing import Any


class Config:
    """
    Loads AIRI configuration files.
    """

    def __init__(self):
        self.config_dir = Path("config")

        self.personality = self._load("personality.json")
        self.settings = self._load("settings.json")
        self.prompts = self._load("prompts.json")
        self.relationship = self._load("relationship.json")

    def _load(self, filename: str) -> dict[str, Any]:
        path = self.config_dir / filename

        if not path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {path}"
            )

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)