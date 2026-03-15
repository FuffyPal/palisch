# Palisch Language Converter Tasks

- [x] Phase 1: Project Setup and Configuration
  - [x] Create `/home/fluffypal/Projects/palisch` directory (or use if existing)
  - [x] Prepare necessary Python file structure (`main.py`, `src/converter.py` etc.)
- [x] Phase 2: Core Converter Logic
  - [x] Define character replacement rule dictionary (R->W, S/Ş->Sch etc.)
  - [x] Include text conversion algorithms in `src/converter.py` using mathematical and string operations (Case-sensitivity will be added)
- [x] Phase 3: CLI (Command Line) Integration
  - [x] Set up command line arguments (`-t`, `--text`) in `main.py` using the `argparse` library
  - [x] Send text from argument to conversion function and print result to terminal
- [x] Phase 4: Manual Test and Verification
  - [x] Perform manual test with sample words like `python main.py -t "Rüzgar Şelale"` and verify results match rules
- [x] Phase 5: Interactive Mode (TUI) Support
  - [x] Implement fallback to interactive `input()` if no CLI arguments are provided
  - [x] Ensure the experience is user-friendly for non-CLI users
