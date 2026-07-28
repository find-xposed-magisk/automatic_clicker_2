# Repository Guidelines

## Project Structure & Module Organization
- Entry point: `main.py` (GUI app startup).
- Core logic: `main_work.py`, `功能类.py`, `functions.py`, `数据库操作.py`.
- Window controllers: `WindowControl/`; application metadata: `info.py`.
- UI resources: `Window/` for `.ui` and generated `*_ui.py` files.
- Assets & themes: `flat/`, `Window/flatwhite/`, `clicker.ico`, `images.qrc`, `images_rc.py`.
- Data/config: `config.ini`, `命令集.db`.
- Tests/experiments: `test_1.py`, `test_2.py`, `test_3.py`, `测试单元.py`.
- Packaging: `Clicker.spec`, `打包指令.md`.

## Build, Test, and Development Commands
- Install deps: `pip install -r requirements.txt`.
- Run locally: `python main.py`.
- Packaging: follow `打包指令.md` (PyInstaller/Nuitka setup is referenced in `requirements.txt`).

## Coding Style & Naming Conventions
- Python codebase; use 4-space indentation.
- Filenames mix English and Chinese; keep new module names consistent with existing naming.
- UI files: keep `.ui` in `Window/` and generated `*_ui.py` alongside them.
- No formatter/linter is configured; keep changes minimal and consistent with surrounding code.

## Testing Guidelines
- No formal test framework detected; tests are script-style.
- Add quick checks in `test_*.py` or `测试单元.py` and document how to run them.
- Run a test script directly: `python test_1.py`.

## Commit & Pull Request Guidelines
- Existing commits use short Chinese descriptions or timestamps (e.g., `2025年2月5日23:59:01`).
- Use concise, descriptive messages in the same style.
- PRs: check `.gitee/PULL_REQUEST_TEMPLATE.zh-CN.md` and include a clear summary, steps to verify, and screenshots if UI changes.

## Configuration Tips
- Keep `config.ini` and `命令集.db` out of functional diffs unless you are intentionally changing defaults or seed data.
