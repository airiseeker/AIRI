from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """Abstract interface for language models."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from the given prompt."""
        raise NotImplementedError