# CampusNotes – Python Project

CampusNotes is a command-line note manager for students, built using Python.
It supports adding, viewing, searching, updating, deleting, and filtering notes by subject.
Notes are stored locally in a JSON file.

## Project structure

```text
CampusNotes_Python/
├── main.py
├── campusnotes/
│   ├── __init__.py
│   ├── notes_manager.py
│   └── storage.py
├── data/
│   └── notes.json
├── tests/
│   └── test_notes_manager.py
└── README.md
```

## Run in VS Code

1. Extract the ZIP file.
2. Open the `CampusNotes_Python` folder in VS Code.
3. Open Terminal → New Terminal.
4. Run:

```bash
python main.py
```

No external packages are required.

## Run the tests

From the project root:

```bash
python -m unittest discover -s tests
```

## Features

- Add notes with a subject and content.
- View all saved notes.
- Search notes by keyword.
- Update an existing note.
- Delete a note by ID.
- Filter notes by subject.
- Save notes between runs using `data/notes.json`.

## Troubleshooting

- Make sure Python is installed before running CampusNotes.
- Check Python using python --version.
- Run commands from the main project directory.
- Make sure the data folder is available.

## Contribution Guidelines

Contributions to CampusNotes are welcome.
Test your updates before submitting changes and provide a clear description of improvements.
