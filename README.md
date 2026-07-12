![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)

# fih

**SUCA** (slightly-useful-cli-apps) is a Python terminal application that bundles a few small utility tools into one interactive command-line interface. It runs as a loop where you type commands to access each tool.

---

## Requirements

- Python 3.12 or newer

No third-party packages are required. The app uses only the Python standard library (`sqlite3`, `datetime`, `pathlib`, `math`, `random`).

---

## Running

```
python main.py
```

Once running, type `help` to list available commands.

---

## Commands

| Command | Description                        |
|---------|------------------------------------|
| `calc`  | Opens the calculator               |
| `note`  | Opens the notes manager            |
| `color` | Not yet implemented                |
| `help`  | Lists available commands           |
| `exit`  | Exits the application              |

---

## Calculator

Supports basic arithmetic on integers.

```
calc
What operation?
+ - * /
```

Enter an operator, then provide two numbers when prompted. Supported operations: `+` (add), `-` (subtract), `*` (multiply), `/` (divide).

---

## Notes

A simple note-taking system backed by a local SQLite database. Notes are stored at:

```
%USERPROFILE%\.suca\databases\notes.db   (Windows)
~/.suca/databases/notes.db               (Linux / macOS)
```

### Notes commands

| Command  | Description                       |
|----------|-----------------------------------|
| `add`    | Create a new note                 |
| `list`   | List all notes (ID, title, date)  |
| `view`   | View a note by ID                 |
| `delete` | Delete a note by ID               |
| `help`   | Lists notes commands              |
| `exit`   | Return to the main menu           |

Each note has a title, content, tags (comma-separated), and a creation timestamp.

---

## Building

Releases are built automatically via GitHub Actions using PyInstaller when a version tag (`v*`) is pushed. Binaries are produced for Windows, Linux, and macOS.

To build manually:

```powershell
pip install pyinstaller
pyinstaller --onefile --clean --name suca main.py
```

The output binary will be in the `dist\` folder.

---

## License

[CC BY-NC 4.0](LICENSE) - Non-commercial use only.
