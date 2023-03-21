def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    counter = 1
    result = ""
    while counter <= n:
        n_spaces = (int((n-counter)/2))
        if counter != n:
            result += " " * n_spaces
        result += "*" * counter + "\n"
        counter += 2
    counter -= 4
    while counter >= 1:
        n_spaces = (int((n-counter)/2))
        result += " " * n_spaces
        result += "*" * counter + "\n"
        counter -= 2
    return result

print(diamond(5))