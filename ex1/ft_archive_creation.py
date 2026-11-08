
import sys


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) != 2:
        print("Usage: python3 ft_archive_creation.py <filename>")
        return

    filename: str = sys.argv[1]

    try:
        print(f"Accessing file '{filename}'")

        file = open(filename, "r")
        content: str = file.read()
        file.close()

        print("---")
        print("")
        print(content, end="")
        if not content.endswith("\n"):
            print()
        print("")
        print("---")
        print(f"File '{filename}' closed.")
        print("")

        print("Transform data:")
        print("---")
        print("")

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
        print("")
        print("---")

        new_filename: str = input("Enter new file name (or empty): ")

        if new_filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            new_file = open(new_filename, "w")
            new_file.write(transformed)
            new_file.close()
            print(f"Data saved in file '{new_filename}'.")

    except OSError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
