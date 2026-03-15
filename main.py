import argparse
from src.converter import convert_text
import sys

def main():
    parser = argparse.ArgumentParser(description="Palisch Language Converter CLI tool")
    parser.add_argument("-t", "--text", type=str, required=True, help="Text to be converted")

    if len(sys.argv) == 1:
        print("--- Palisch Interactive Mode ---")
        print("Type your text and press Enter to convert.")
        print("Press Ctrl+C or type 'exit' to quit.")
        try:
            while True:
                text = input("\n> ")
                if text.lower() == 'exit':
                    break
                if not text.strip():
                    continue
                converted = convert_text(text)
                print(f"Palisch: {converted}")
        except KeyboardInterrupt:
            print("\nExiting...")
        return
    
    args = parser.parse_args()
    
    converted = convert_text(args.text)
    print(converted)

if __name__ == "__main__":
    main()
