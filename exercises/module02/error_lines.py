def error_lines(path):
    # TODO: yield matching lines without reading the whole file at once
    raise NotImplementedError


if __name__ == "__main__":
    for line in error_lines("sample.log"):
        print(line, end="")
