def array_diff(a, b):
    if len(a) == 0 or len(b) == 0:
        return a
    result = a.copy()
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                if a[j] in result:
                    result.remove(a[j])
    return result
