import tempfile
import unittest
from pathlib import Path

from campusnotes.notes_manager import NotesManager
from campusnotes.storage import NotesStorage


class NotesManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        storage = NotesStorage(Path(self.temp_dir.name) / "notes.json")
        self.manager = NotesManager(storage)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_search_note(self):
        self.manager.add_note("Python", "Lists store multiple values.")
        results = self.manager.search_notes("lists")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["subject"], "Python")

    def test_update_note(self):
        note = self.manager.add_note("Java", "Classes are blueprints.")
        self.assertTrue(self.manager.update_note(note["id"], "Java OOP", "Objects are instances."))
        self.assertEqual(self.manager.notes[0]["subject"], "Java OOP")

    def test_delete_note(self):
        note = self.manager.add_note("Maths", "Study matrices.")
        self.assertTrue(self.manager.delete_note(note["id"]))
        self.assertEqual(self.manager.notes, [])

    def test_empty_note_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_note("", "Some content")


if __name__ == "__main__":
    unittest.main()
