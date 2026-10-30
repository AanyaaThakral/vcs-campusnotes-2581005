import json
from pathlib import Path


class NotesStorage:
    """Handles reading and writing notes to a JSON file."""

    def __init__(self, file_path="data/notes.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def load(self):
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def save(self, notes):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
