from datetime import datetime
from campusnotes.storage import NotesStorage


class NotesManager:
    """Contains the operations used to manage student notes."""

    def __init__(self, storage=None):
        self.storage = storage or NotesStorage()
        self.notes = self.storage.load()
        self.next_id = max((note.get("id", 0) for note in self.notes), default=0) + 1

    def add_note(self, subject, content):
        if not subject.strip() or not content.strip():
            raise ValueError("Subject and note content cannot be empty.")

        note = {
            "id": self.next_id,
            "subject": subject.strip(),
            "content": content.strip(),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.notes.append(note)
        self.next_id += 1
        self.storage.save(self.notes)
        return note

    def search_notes(self, keyword):
        keyword = keyword.lower().strip()
        if not keyword:
            return []
        return [
            note for note in self.notes
            if keyword in note["subject"].lower()
            or keyword in note["content"].lower()
        ]

    def update_note(self, note_id, subject, content):
        if not subject.strip() or not content.strip():
            raise ValueError("Subject and note content cannot be empty.")

        for note in self.notes:
            if note["id"] == note_id:
                note["subject"] = subject.strip()
                note["content"] = content.strip()
                note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                self.storage.save(self.notes)
                return True
        return False

    def delete_note(self, note_id):
        for index, note in enumerate(self.notes):
            if note["id"] == note_id:
                del self.notes[index]
                self.storage.save(self.notes)
                return True
        return False

    def get_by_subject(self, subject):
        subject = subject.lower().strip()
        return [
            note for note in self.notes
            if note["subject"].lower() == subject
        ]

    @staticmethod
    def display_notes(notes):
        if not notes:
            print("\nNo notes found.")
            return

        print("\n--------- YOUR NOTES ---------")
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Subject: {note['subject']}")
            print(f"Content: {note['content']}")
            print(f"Created: {note.get('created_at', 'Unknown')}")
            if note.get("updated_at"):
                print(f"Updated: {note['updated_at']}")
            print("------------------------------")
