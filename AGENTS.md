# Repository Guidelines

## Project Structure & Module Organization
`Clicker.py` is the desktop app entry point and wires together the main PySide6 window, hotkeys, settings, and update flow. Core execution logic lives in `main_work.py`, `功能类.py`, `数据库操作.py`, and `ini控制.py`. UI definitions are stored under `窗体/`; generated `*_ui.py` files should stay aligned with their matching `.ui` sources. Static assets live in `flat/`, `窗体/res/`, and `clicker.ico`. Packaging files include `Clicker.spec`, `pyproject.toml`, `requirements.txt`, and `uv.lock`.

## Build, Test, and Development Commands
Use Python 3.12 in a virtual environment.

- `uv sync` installs dependencies from `pyproject.toml` and `uv.lock`.
- `pip install -r requirements.txt` is the fallback setup path.
- `python Clicker.py` launches the application locally.
- `pyinstaller Clicker.spec` builds the packaged executable.
- `python test_2.py` or `python test_3.py` runs the existing ad hoc verification scripts.

`打包指令.md` also contains maintained Nuitka commands for Windows release builds.

## Coding Style & Naming Conventions
Follow the existing code style: 4-space indentation, UTF-8 source files, and concise docstrings for non-obvious behavior. Keep module names consistent with the current mixed Chinese naming scheme, and use `snake_case` for functions, variables, and new helper modules. Use `PascalCase` for Qt window and worker classes such as `Main_window` and `CommandThread`. Prefer explicit imports over new wildcard imports, especially outside legacy files.

## Testing Guidelines
This repository does not yet have a formal `pytest` suite. Treat `test_*.py` as manual or exploratory checks, not coverage gates. For changes to commands, verify at minimum that `python Clicker.py` starts cleanly, the edited window opens, and the affected automation flow runs against a disposable test case. Add focused script-based repro tests when fixing bugs in parsing, config, or database behavior.

## Commit & Pull Request Guidelines
Recent history uses short, task-focused commit subjects, often in Chinese, for example `ini和数据库控制封装为class` and `UI`. Keep commits small and descriptive; one change set per commit. Pull requests should summarize the user-visible behavior change, list touched modules, note any config or database impact, and include screenshots for UI edits. Link the related issue when one exists.

## Configuration & Safety Tips
Do not commit machine-specific secrets or local runtime data from `config.ini` and `命令集.db`. Test automation changes on non-critical apps first; this project can control the mouse, keyboard, browser, and windows globally.
