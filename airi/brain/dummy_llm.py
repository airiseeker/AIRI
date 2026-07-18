from .llm import BaseLLM


class DummyLLM(BaseLLM):
    """Simple LLM used during development."""

    def generate(self, prompt: str) -> str:
        """Return a fixed response."""

        print("\n===== PROMPT =====")
        print(prompt)
        print("==================")

        return (
            "Halo Papah! 🌸\n"
            "Aku berhasil memahami apa yang kamu katakan."
        )