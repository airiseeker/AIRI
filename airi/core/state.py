from enum import Enum


class AiriState(Enum):

    CREATED = "Created"

    INITIALIZING = "Initializing"

    IDLE = "Idle"

    LISTENING = "Listening"

    THINKING = "Thinking"

    SPEAKING = "Speaking"

    SLEEPING = "Sleeping"