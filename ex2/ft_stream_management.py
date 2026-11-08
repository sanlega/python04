import sys


def main():
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) != 2:
        print(
            "[STDERR] Usage: python3 ft_stream_management.py <filename>",
            file=sys.stderr
        )
        return

    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
    except OSError as error:
        print(
            f"[STDERR] Error opening file '{filename}': {error}",
            file=sys.stderr
        )
        return

    print("---")
    print(content, end="")
    if not content.endswith("\n"):
        print()
    print("---")
    print(f"File '{filename}' closed.")

    print("Transform data:")
    print("---")

    transformed = ""
    line = ""

    for char in content:
        if char == "\n":
            transformed += line + "#\n"
            line = ""
        else:
            line += char

    if line:
        transformed += line + "#"

    print(transformed, end="")
    if not transformed.endswith("\n"):
        print()
    print("---")

    print("Enter new file name (or empty): ", end="", flush=True)
    new_filename = sys.stdin.readline().rstrip("\n")

    if new_filename == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")

    try:
        new_file = open(new_filename, "w")
        new_file.write(transformed)
        new_file.close()
        print(f"Data saved in file '{new_filename}'.")
    except OSError as error:
        print(
            f"[STDERR] Error opening file '{new_filename}': {error}",
            file=sys.stderr
        )
        print("Data not saved.")


if __name__ == "__main__":
    main()
