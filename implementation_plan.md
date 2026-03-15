# Goal

Develop a tool (CLI tool) that converts text into the Palisch language based on user-defined language rules (R->W, S/Ş->Sch etc.). The tool supports both single-shot CLI execution via `python main.py -t "text"` and an interactive mode (TUI) via `python main.py`.

## Proposed Changes

The following tree structure will be established under the current project directory (`/home/fluffypal/Projects/palisch`) to facilitate coding:

```text
palisch/
├── main.py
└── src/
    ├── __init__.py
    └── converter.py
```

---

### Core Logic

#### [NEW] src/__init__.py
An empty file will be created so that the `src` directory is recognized as a Python package.

#### [NEW] src/converter.py
This file will contain the `convert_text(text: str) -> str` function. Transformation rules will be applied Case-Sensitively:
* R, r -> W, w
* S, s, Ş, ş -> Sch, sch
* Z, z -> tz (Tz for uppercase Z, tz for lowercase z)
* K, k -> Q, q
* G, g -> C, c
* L, l -> Ly, ly

#### [NEW] main.py
Main file where the application will run. A command-line interface will be created using the `argparse` module.
The script handles two modes:
1. **CLI Mode**: Text from `-t` or `--text` parameters is taken, converted, and printed.
2. **Interactive Mode (TUI)**: If no arguments are provided, the user is prompted to enter text interactively. This provides a simpler interface for multiple or quick conversions without flags.

## Verification Plan

### Manual Verification
CLI commands will be tested via Terminal:
- Running the `python main.py -t "Rüzgar Şelale"` command.
- Testing the successful application of rules and conversion of characters. Words of different lengths (Zaman, Kalem, Gölge) will be tried to verify expected results.
