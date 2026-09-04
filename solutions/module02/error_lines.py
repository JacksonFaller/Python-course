def error_lines(path):
    with open(path, encoding="utf-8") as file:
        for line in file:
            if "ERROR" in line:
                yield line
