def last_line(file_name: str):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        try:
            if not lines[-1].endswith("\n"):
                lines[-1] += "\n"
            for text_line in reversed(lines):
                yield repr(text_line)
        except IndexError:
            raise Exception("Text file is empty")


if __name__ == "__main__":
    txt_file = "last_line.txt"
    for line in last_line(file_name=txt_file):
        print(line, end="\n")
