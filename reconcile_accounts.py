def last_lines(file_name: str):
    with open(file_name, "r") as file:
        lines = file.readlines()
        if not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        for text_line in reversed(lines):
            yield repr(text_line)


if __name__ == "__main__":
    for line in last_lines("last_line.txt"):
        print(line, end="\n")
