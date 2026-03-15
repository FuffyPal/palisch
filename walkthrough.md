# Palisch Language Converter - Application Summary

CLI and String converter core logic successfully completed. Implemented using the `src` directory approach.

## Implemented Changes
- **Folder Structure:** Files gathered under `src` directory (added [src/__init__.py](file:///home/fluffypal/Projects/palisch/src/__init__.py) and [src/converter.py](file:///home/fluffypal/Projects/palisch/src/converter.py)).
- **Core Algorithm:** Case-sensitive rules implemented in [convert_text](file:///home/fluffypal/Projects/palisch/src/converter.py#L1-L39) function within [src/converter.py](file:///home/fluffypal/Projects/palisch/src/converter.py).
- **CLI Module:** Added `-t` / `--text` parameter control to [main.py](file:///home/fluffypal/Projects/palisch/main.py) with the `argparse` library. Application is now directly usable from a terminal interface.
- **Interactive Mode (TUI):** Added a fallback mechanism in [main.py](file:///home/fluffypal/Projects/palisch/main.py) that allows users to run the application without arguments to enter an interactive session.

## Verification Results
Tests were performed using the string `Rüzgar Şelale` via both CLI and Interactive modes, and the following output was obtained in full compliance with the rules:
> **Wützcaw Schelyalye**

It has been verified that the application performs conversions without issues and follows case-sensitivity rules. You can use it from your terminal anytime with the `python main.py -t "Desired Text"` command or simply `python main.py` for interactive mode.
