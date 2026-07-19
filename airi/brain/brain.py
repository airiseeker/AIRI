from .context_builder import ContextBuilder
from .dummy_llm import DummyLLM
from .prompt_builder import PromptBuilder
from airi.personality import Personality
from airi.relationship import Relationship
from .llm import BaseLLM

class Brain:

    def __init__(
        self,
        personality: Personality,
        relationship: Relationship,
        llm: BaseLLM,
    ) -> None:

        self.personality = personality
        self.relationship = relationship
        
        self.prompt_builder = PromptBuilder()
        self.context_builder = ContextBuilder()
        self.llm = llm

    def think(self, user_message: str) -> str:
        """
        Generate a response from the user's message.
        """

        context = self.context_builder.build()

        prompt = self.prompt_builder.build(
            personality=self.personality,
            relationship=self.relationship,
            context=context,
            user_message=user_message,
        )

        response = self.llm.generate(prompt)

        return response