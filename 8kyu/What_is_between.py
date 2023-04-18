def between(a,b):
    result = []
    counter = 0
    for i in range(b-a+1):
        result.append(a + counter)
        counter += 1
    return result
        