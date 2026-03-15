# Palisch Language Converter

A command-line interface (CLI) tool designed to convert text into the Palisch language based on specific character transformation rules.

## Features

- **Interactive Mode (TUI)**: Runs a simple interactive session if no arguments are provided.
- **Case-Sensitive Transformation**: Preserves the casing of the original text.
- **Custom Rules**: Implements specific phonetic and character mapping rules.
- **Easy to Use**: Simple CLI parameters or interactive prompt for quick conversions.

## Transformation Rules

The tool follows these primary conversion rules:
- **R, r** → **W, w**
- **S, s, Ş, ş** → **Sch, sch**
- **Z, z** → **Tz, tz**
- **K, k** → **Q, q**
- **G, g** → **C, c**
- **L, l** → **Ly, ly**

## Installation

Ensure you have Python installed. Clone the repository and navigate to the project directory.

```bash
git clone <repository-url>
cd palisch
```

## Usage

### CLI Mode

Run the converter using the `-t` flag for single-shot conversion:

```bash
python main.py -t "Your text here"
```

### Interactive Mode (TUI)

Simply run the script without any arguments to enter the interactive mode:

```bash
python main.py
```

### Example

**CLI:**
```bash
python main.py -t "Rüzgar Şelale"
# Output: Wützcaw Schelyalye
```

**Interactive:**
```text
--- Palisch Interactive Mode ---
Type your text and press Enter to convert.
Press Ctrl+C or type 'exit' to quit.

> Rüzgar
Palisch: Wützcaw

> Şelale
Palisch: Schelyalye
```

## Project Structure

```text
palisch/
├── main.py           # Entry point for the CLI
├── src/
│   ├── __init__.py   # Python package initialization
│   └── converter.py  # Core transformation logic
├── task.md           # Project task tracking
├── implementation_plan.md # Development roadmap
└── walkthrough.md    # Summary of changes and verification
```

## License

This project is open-source and available for use under the MIT License.
