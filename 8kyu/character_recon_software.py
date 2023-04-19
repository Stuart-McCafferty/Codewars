def correct(s):
    result = ""
    for i in range(len(s)):
        if s[i] == "5":
            result += "S"
        elif s[i] == "0":
            result += "O"
        elif s[i] == "1":
            result += "I"
        else:
            result += s[i]
    return result