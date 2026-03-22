from collections import Counter


def read_lines(filename: str) -> list[str]:
    """Read all lines from a text file and return them as a list."""
    with open(filename, "r") as file:
        return file.readlines()


def write_lines(filename: str, lines: list[str]) -> None:
    """Write a list of lines to a text file."""
    with open(filename, "w") as file:
        file.writelines(lines)


def count_words(filename: str) -> dict[str, int]:
    """Count occurrences of each word in a text file."""
    with open(filename, "r") as file:
        text = file.read().lower()

    words = text.split()
    words = [word for word in words if word]
    return dict(Counter(words))
