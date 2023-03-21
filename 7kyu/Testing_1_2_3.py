def number(lines):
    if len(lines) == 0:
        return lines
    result = []
    for i in range(1, len(lines) + 1):
        result.append(str(i) + ": " + lines[i - 1])
    return result