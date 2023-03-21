def expanded_form(num):
    num = str(num)
    result = ""
    counter = 0
    for i in range(len(num), 0, -1):
        if num[counter] != "0":
            result += num[counter] 
            result += "0" * (i-1) + " + "
        counter += 1
    return result[:-2]

print(expanded_form(70304))
