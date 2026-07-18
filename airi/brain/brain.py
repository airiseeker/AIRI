from .context_builder import ContextBuilder
from .dummy_llm import DummyLLM
from .prompt_builder import PromptBuilder


class Brain:
    """Coordinate the thinking process."""

    def __init__(self) -> None:
        """Initialize brain components."""

        self.prompt_builder = PromptBuilder()
        self.context_builder = ContextBuilder()
        self.llm = DummyLLM()

    def think(self, user_message: str) -> str:
        """
        Generate a response from the user's message.
        """

        context = self.context_builder.build()

        prompt = self.prompt_builder.build(
            user_message=user_message
        )

        response = self.llm.generate(prompt)

        return response