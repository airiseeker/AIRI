class PromptBuilder:
    """Build prompts for the language model."""

    def build(self, user_message: str) -> str:
        """Construct a prompt from the user's message."""

        return f"""
Kamu adalah AIRI.

Namamu AIRI.

Jawablah dengan ramah dan natural.

Papah berkata:
{user_message}
"""