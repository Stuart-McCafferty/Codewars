def solution(text, ending):
    length = len(ending)
    if (text[-length:] == ending):
        return True
    else:
        return False

print(solution("sumo", "mo"))



# CAN YOU END WITH 