def friend(x):
    result = []
    for i in range(len(x)):
        if len(x[i]) == 4:
            result.append(x[i])
    
    return result