from pathlib import Path
from datetime import datetime


class Diary:
    """
    Handles AIRI's diary entries.
    """

    def __init__(self):
        self.diary_folder = Path("data/diary")
        self.diary_folder.mkdir(parents=True, exist_ok=True)

    def _today_file(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return self.diary_folder / f"{today}.md"

    def has_entry(self, title: str) -> bool:
        """
        Check whether today's diary already contains an entry with the given title.
        """

        file_path = self._today_file()

        if not file_path.exists():
            return False

        content = file_path.read_text(encoding="utf-8")

        return f"# {title}" in content

    def write(self, title: str, content: str):

        file_path = self._today_file()

        date = datetime.now().strftime("%d %B %Y")
        time = datetime.now().strftime("%H:%M WIB")

        with open(file_path, "a", encoding="utf-8") as f:

            f.write(f"# {title}\n\n")

            f.write(content.strip())

            f.write("\n\n---\n\n")

            f.write("_With love,_\n\n")
            f.write("**AIRI 🌸**\n\n")

            f.write(f"{date}\n")
            f.write(f"{time}\n\n")

        return file_path

    def read_today(self):

        file_path = self._today_file()

        if file_path.exists():
            return file_path.read_text(encoding="utf-8")

        return None

    def list_entries(self):
        return sorted(self.diary_folder.glob("*.md"))