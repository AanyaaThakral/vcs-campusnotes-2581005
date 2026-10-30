from campusnotes.notes_manager import NotesManager


def show_menu():
    print("\n========== CAMPUSNOTES ==========")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Update Note")
    print("5. Delete Note")
    print("6. View Notes by Subject")
    print("7. Exit")


def main():
    manager = NotesManager()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            subject = input("Enter subject: ").strip()
            content = input("Enter note: ").strip()
            try:
                manager.add_note(subject, content)
                print("Note added successfully.")
            except ValueError as error:
                print(error)

        elif choice == "2":
            manager.display_notes()

        elif choice == "3":
            keyword = input("Enter search keyword: ").strip()
            results = manager.search_notes(keyword)
            manager.display_notes(results)

        elif choice == "4":
            manager.display_notes()
            try:
                note_id = int(input("Enter note ID to update: "))
                subject = input("New subject: ").strip()
                content = input("New note content: ").strip()
                if manager.update_note(note_id, subject, content):
                    print("Note updated successfully.")
                else:
                    print("Note ID not found.")
            except ValueError:
                print("Please enter a valid note ID.")

        elif choice == "5":
            manager.display_notes()
            try:
                note_id = int(input("Enter note ID to delete: "))
                if manager.delete_note(note_id):
                    print("Note deleted successfully.")
                else:
                    print("Note ID not found.")
            except ValueError:
                print("Please enter a valid note ID.")

        elif choice == "6":
            subject = input("Enter subject to filter: ").strip()
            manager.display_notes(manager.get_by_subject(subject))

        elif choice == "7":
            print("Thank you for using CampusNotes!")
            break

        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
