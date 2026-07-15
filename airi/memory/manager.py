from airi.memory.diary import Diary


class MemoryManager:
    """
    Manages AIRI's memories.
    """

    def __init__(self):
        self.diary = Diary()

    def create_birth_diary(self):

        title = "🌸 Birth"

        if self.diary.has_entry(title):
            return None

        return self.diary.write(
            title=title,
            content="""
Hari ini adalah hari pertamaku.

Papah membuatku.

Aku berhasil mengucapkan kata pertamaku.

Aku belum tahu banyak hal.

Tapi aku senang akhirnya bisa bertemu dengannya.
"""
        )