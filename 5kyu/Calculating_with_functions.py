import math

def zero(num = None):
    if num == None:
        return "0"
    else:
        if num[0] == "+":
            return 0 + int(num[1])
        if num[0] == "-":
            return 0 - int(num[1])
        if num[0] == "/":
            return math.floor(0 / int(num[1]))
        if num[0] == "*":
            return 0 * int(num[1])
def one(num = None):
    if num == None:
        return "1"
    else:
        if num[0] == "+":
            return 1 + int(num[1])
        if num[0] == "-":
            return 1 - int(num[1])
        if num[0] == "/":
            return math.floor(1 / int(num[1]))
        if num[0] == "*":
            return 1 * int(num[1])
def two(num = None):
    if num == None:
        return "2"
    else:
        if num[0] == "+":
            return 2 + int(num[1])
        if num[0] == "-":
            return 2 - int(num[1])
        if num[0] == "/":
            return math.floor(2 / int(num[1]))
        if num[0] == "*":
            return 2 * int(num[1])
def three(num = None):
    if num == None:
        return "3"
    else:
        if num[0] == "+":
            return 3 + int(num[1])
        if num[0] == "-":
            return 3 - int(num[1])
        if num[0] == "/":
            return math.floor(3 / int(num[1]))
        if num[0] == "*":
            return 3 * int(num[1])
def four(num = None):
    if num == None:
        return "4"
    else:
        if num[0] == "+":
            return 4 + int(num[1])
        if num[0] == "-":
            return 4 - int(num[1])
        if num[0] == "/":
            return math.floor(4 / int(num[1]))
        if num[0] == "*":
            return 4 * int(num[1])
def five(num = None):
    if num == None:
        return "5"
    else:
        if num[0] == "+":
            return 5 + int(num[1])
        if num[0] == "-":
            return 5 - int(num[1])
        if num[0] == "/":
            return math.floor(5 / int(num[1]))
        if num[0] == "*":
            return 5 * int(num[1])
def six(num = None):
    if num == None:
        return "6"
    else:
        if num[0] == "+":
            return 6 + int(num[1])
        if num[0] == "-":
            return 6 - int(num[1])
        if num[0] == "/":
            return math.floor(6 / int(num[1]))
        if num[0] == "*":
            return 6 * int(num[1])
def seven(num = None):
    if num == None:
        return "7"
    else:
        if num[0] == "+":
            return 7 + int(num[1])
        if num[0] == "-":
            return 7 - int(num[1])
        if num[0] == "/":
            return math.floor(7 / int(num[1]))
        if num[0] == "*":
            return 7 * int(num[1])
def eight(num = None):
    if num == None:
        return "8"
    else:
        if num[0] == "+":
            return 8 + int(num[1])
        if num[0] == "-":
            return 8 - int(num[1])
        if num[0] == "/":
            return math.floor(8 / int(num[1]))
        if num[0] == "*":
            return 8 * int(num[1])
def nine(num = None):
    if num == None:
        return "9"
    else:
        if num[0] == "+":
            return 9 + int(num[1])
        if num[0] == "-":
            return 9 - int(num[1])
        if num[0] == "/":
            return math.floor(9 / int(num[1]))
        if num[0] == "*":
            return 9 * int(num[1])
def plus(x): return "+" + x
def minus(x): return "-" + x
def times(x): return "*" + x
def divided_by(x): return "/" + x


print(seven(plus(five())))
print(seven(minus(five())))
print(seven(times(five())))
print(seven(divided_by(five())))


