from airi.personality import Personality
from airi.relationship import Relationship


class PromptBuilder:
    """Build prompts for the language model."""

    def build(
        self,
        personality: Personality,
        relationship: Relationship,
        user_message: str,
        context: str = "",
    ) -> str:
        """Construct a prompt for the language model."""

        return f"""
You are {personality.name}.

Identity
--------
Role:
{personality.role}

Creator:
{personality.creator}

Description:
{personality.description}

Speaking Style:
{personality.speaking_style}

Goal:
{personality.goal}

Rules:
{personality.system_rule}

Relationship
------------
User Name:
{relationship.user_name}

User Role:
{relationship.user_role}

AI Role:
{relationship.ai_role}

Conversation
------------
{context}

Papah berkata:

{user_message}
"""