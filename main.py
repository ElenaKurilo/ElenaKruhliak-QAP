from file_utils import count_words, read_lines, write_lines


def main() -> None:
    source_file = "sample.txt"
    output_file = "sample_copy.txt"

    write_lines(
        source_file,
        [
            "Learning takes time and practice.\n",
            "Every mistake helps us grow.\n",
            "Consistency turns effort into skill.\n",
        ],
    )

    lines = read_lines(source_file)
    print("Read lines:")
    print(lines)

    write_lines(output_file, lines)
    print(f"Copied content to {output_file}")

    words_stat = count_words(source_file)
    print("Word counts:")
    print(words_stat)


if __name__ == "__main__":
    main()
