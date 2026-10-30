import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accesing file '{sys.argv[1]}'")
    try:
        file = open(sys.argv[1])
        print("---")
        print("")
        buffer = file.read(1)
        while buffer:
            print(buffer, end='')
            buffer = file.read(1)
        print("")
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
